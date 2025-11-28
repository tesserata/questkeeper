from qk_api_contracts.schema.characters import (
    Character,
    CharacterRead,
)

from app.domain.characters import Character as DomainCharacter


def character_base_to_domain(character_base: Character) -> DomainCharacter:
    return DomainCharacter(
        user_id=None,
        system=character_base.system,
        name=character_base.name,
        class_name=character_base.class_name,
        subclass_name=character_base.subclass_name,
        level=character_base.level,
        race=character_base.race,
    )


def character_domain_to_read(character: DomainCharacter) -> CharacterRead:
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
