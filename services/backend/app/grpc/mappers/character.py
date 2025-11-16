from qk_api_contracts.grpc.characters.models_pb2 import CharacterSummary

from app.domain.characters import Character as DomainCharacter


def character_domain_to_summary_pb(domain: DomainCharacter) -> CharacterSummary:
    return CharacterSummary(
        character_id=str(domain.character_id),
        name=domain.name,
        class_name=domain.class_name,
        key_attribute=domain.key_attribute,
    )
