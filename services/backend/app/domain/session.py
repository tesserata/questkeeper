from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4

from qk_api_contracts.enums import GameSystem, ScheduleStatus, SignupRole

from app.domain.common import VersionHeader


# -------- Domain errors --------
class DomainError(Exception): ...


class AlreadySignedUp(DomainError): ...


class NotSignedUp(DomainError): ...


class SeatUnavailable(DomainError): ...


class InvalidTransition(DomainError): ...


class InvariantViolation(DomainError): ...


@dataclass
class Signup:
    session_id: UUID
    user_id: int
    role: SignupRole
    character_id: UUID | None = None

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def touch(self) -> None:
        self.updated_at = datetime.now(UTC)


# -------- Aggregate root --------
@dataclass
class Session:
    server_id: int
    event_id: UUID | None
    gm_user_id: int

    title: str
    summary: str
    capacity: int

    vtt_link: str | None
    location: str | None

    system: GameSystem = field(default=GameSystem.PATHFINDER_2E)
    additional_links: Iterable[str] = field(default_factory=list)
    role_mentions: Iterable[str] = field(default_factory=list)

    session_id: UUID = field(default_factory=uuid4)

    status: ScheduleStatus = field(default=ScheduleStatus.SCHEDULED)
    time: datetime = field(default_factory=lambda: datetime.now(UTC))
    duration_minutes: int = field(default=3 * 60)

    channel_id: int | None = field(default=None)
    message_id: int | None = field(default=None)
    version_header: VersionHeader = field(default_factory=VersionHeader)

    signups: dict[str, Signup] = field(default_factory=dict)

    # ---------- Queries ----------
    def main_active_count(self) -> int:
        return sum(1 for s in self._active_signups() if s.role == SignupRole.MAIN)

    def has_active_signup(self, user_id: str) -> bool:
        s = self.signups.get(user_id)
        return bool(s)

    def get_signup(self, user_id: str) -> Signup:
        s = self.signups.get(user_id)
        if not s:
            raise NotSignedUp(f"user {user_id} has no record for session {self.session_id}")
        return s

    def _active_signups(self) -> Iterable[Signup]:
        return (s for s in self.signups.values() if s.active)

    def _bump_version(self) -> None:
        self.version += 1

    def _assert_invariants(self) -> None:
        # one Active signup per (user, session)
        # (maintained by mapping; enforce at mutation boundaries)
        # main_active ≤ capacity
        if self.main_active_count() > self.capacity:
            raise InvariantViolation(
                f"main_active ({self.main_active_count()}) exceeds capacity ({self.capacity})"
            )
        if self.capacity < 0:
            raise InvariantViolation("capacity cannot be negative")

    # ---------- Commands (all mutate + enforce invariants + bump version) ----------
    def signup(self, *, user_id: str, role: SignupRole, character_id: str | None = None) -> None:
        """
        Manual signup: user picks MAIN or RESERVE.
        Rules:
          - Exactly one Active signup per user.
          - MAIN requires a free seat at commit time.
        """
        if self.has_active_signup(user_id):
            raise AlreadySignedUp(f"user {user_id} already has an active signup")

        if role is SignupRole.MAIN and self.main_active_count() >= self.capacity:
            raise SeatUnavailable("no MAIN seats available")

        self.signups[user_id] = Signup(user_id=user_id, role=role, character_id=character_id)
        self._assert_invariants()
        self._bump_version()

    def switch_main_to_reserve(self, *, user_id: str) -> None:
        """
        Player can switch MAIN → RESERVE (manual model; frees a seat).
        """
        s = self.get_signup(user_id)
        if not s.active:
            raise InvalidTransition("cannot switch: signup is not active")
        if s.role is not SignupRole.MAIN:
            raise InvalidTransition("can only switch MAIN → RESERVE")
        s.role = SignupRole.RESERVE
        s.touch()
        self._assert_invariants()
        self._bump_version()

    def claim_main_from_reserve(self, *, user_id: str) -> None:
        """
        Player can claim a MAIN seat from RESERVE only if a seat is available at click time.
        This is the ONLY allowed RESERVE→MAIN path.
        """
        s = self.get_signup(user_id)
        if not s.active:
            raise InvalidTransition("cannot claim: signup is not active")
        if s.role is not SignupRole.RESERVE:
            raise InvalidTransition("can only claim from RESERVE")
        if self.main_active_count() >= self.capacity:
            raise SeatUnavailable("no MAIN seats available to claim")
        s.role = SignupRole.MAIN
        s.touch()
        self._assert_invariants()
        self._bump_version()

    def leave(self, *, user_id: str) -> None:
        """
        Player leaves the session → their signup becomes inactive (history kept).
        Frees a MAIN seat if they were MAIN.
        """
        s = self.get_signup(user_id)
        if not s.active:
            # idempotent behavior: leaving twice is a no-op
            return
        s.active = False
        s.touch()
        self._assert_invariants()
        self._bump_version()

    def attach_character(self, *, user_id: str, character_id: str | None) -> None:
        """
        Attach or change character on the (active) signup.
        """
        s = self.get_signup(user_id)
        if not s.active:
            raise InvalidTransition("cannot attach character to inactive signup")
        s.character_id = character_id
        s.touch()
        self._bump_version()

    # ---------- Admin / GM ops ----------
    def set_capacity(self, *, new_capacity: int) -> None:
        """
        Adjust capacity. Must not violate main_active ≤ capacity.
        (If you need to shrink below current main_active, force users to switch/leave first.)
        """
        if new_capacity < 0:
            raise InvariantViolation("capacity cannot be negative")
        self.capacity = new_capacity
        # Validate against current state
        self._assert_invariants()
        self._bump_version()
