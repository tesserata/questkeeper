from qk_api_contracts.schema.characters import (
    CharacterBase,
    CharacterRead,
)

from app.domain.character.models import Character


def character_base_to_domain(character_base: CharacterBase) -> Character:
    return Character(
        user_id=None,
        system=character_base.system,
        name=character_base.name,
        class_name=character_base.class_name or "",
        subclass_name=character_base.subclass_name or "",
        level=character_base.level,
        race=character_base.race or "",
    )


def character_domain_to_read(character: Character) -> CharacterRead:
    return CharacterRead(
        character_id=character.character_id,
        user_id=character.user_id,
        system=character.system,
        name=character.name,
        class_name=character.class_name,
        subclass_name=character.subclass_name,
        level=character.level,
        race=character.race,
        notes=character.notes,
    )
