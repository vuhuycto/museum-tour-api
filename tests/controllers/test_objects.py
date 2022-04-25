from main.models.object import ObjectModel
from tests.helpers import (
    OBJECT_BASE_URL,
    TICKET_BASE_URL,
    make_auth_header,
    valid_sale_data,
)
from tests.helpers.braintree import mock_braintree_gateway


def test_find_object_successfully(client, session, mocker):
    mock_braintree_gateway(mocker)
    object_identifier = "a"
    obj = ObjectModel(
        identifier=object_identifier,
        name="a",
        description_url="https://g.com",
    )
    session.add(obj)
    session.commit()

    response = client.post(TICKET_BASE_URL, json=valid_sale_data)
    response = client.get(
        f"{OBJECT_BASE_URL}/{object_identifier}",
        headers=make_auth_header(response),
    )

    assert response.status_code == 200


def test_not_find_object(client, session, mocker):
    mock_braintree_gateway(mocker)

    response = client.post(TICKET_BASE_URL, json=valid_sale_data)
    response = client.get(
        f"{OBJECT_BASE_URL}/a",
        headers=make_auth_header(response),
    )

    assert response.status_code == 404
