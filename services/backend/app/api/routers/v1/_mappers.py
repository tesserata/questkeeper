from qk_api_contracts.schema.characters import (
    Character,
    CharacterBase,
)

from app.domain.characters import Character as DomainCharacter


def character_base_dto_to_domain(character: CharacterBase) -> DomainCharacter:
    return DomainCharacter(
        user_id=None,
        system=character.system,
        name=character.name,
        class_name=character.class_name,
        subclass_name=character.subclass_name,
        level=character.level,
        race=character.race,
        notes=character.notes,
    )


def character_domain_to_dto(character: DomainCharacter) -> Character:
    return Character(
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
