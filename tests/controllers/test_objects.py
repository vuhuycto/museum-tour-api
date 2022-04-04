from main.models.object import ObjectModel

BASE_URL = "/objects/{}"


def test_find_destination_successfully(client, session):
    object_identifier = "a"
    obj = ObjectModel(object_identifier=object_identifier)
    session.add(obj)
    session.commit()

    response = client.get(BASE_URL.format(object_identifier))

    assert response.status_code == 200


def test_not_find_destination(client, session):
    response = client.get(BASE_URL.format("a"))

    assert response.status_code == 404
