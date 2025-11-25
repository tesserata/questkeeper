from app.domain.version import VersionHeader
from app.infrastructure.db.models.base import VersionMixin


def get_version_header(row: VersionMixin) -> VersionHeader:
    return VersionHeader(version=row.version, created_at=row.created_at, updated_at=row.updated_at)
