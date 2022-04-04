from typing import Optional

from main.models.object import ObjectModel


def find_object_by_identifier(identifier: str) -> Optional[ObjectModel]:
    destination = ObjectModel.query.filter(ObjectModel.identifier == identifier).first()
    return destination
