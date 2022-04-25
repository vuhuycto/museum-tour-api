from tests.helpers import (
    TICKET_BASE_URL,
    invalid_jwt,
    invalid_sale_data,
    make_auth_header,
    valid_sale_data,
)
from tests.helpers.braintree import mock_braintree_gateway


def test_create_ticket_successfully(client, mocker):
    mock_braintree_gateway(mocker)

    response = client.post(
        TICKET_BASE_URL,
        json=valid_sale_data,
    )

    assert response.status_code == 200


def test_failed_to_create_ticket(client, mocker):
    response = client.post(
        TICKET_BASE_URL,
        json=invalid_sale_data,
    )
    assert response.status_code == 400

    mock_braintree_gateway(mocker, failure=True)
    response = client.post(
        TICKET_BASE_URL,
        json=valid_sale_data,
    )
    assert response.status_code == 400


def test_validate_ticket_successfully(client, mocker):
    mock_braintree_gateway(mocker)

    response = client.post(TICKET_BASE_URL, json=valid_sale_data)
    response = client.get(
        f"{TICKET_BASE_URL}/validity",
        headers=make_auth_header(response),
    )

    assert response.status_code == 200


def test_validate_ticket_unsuccessfully(client):
    response = client.get(
        f"{TICKET_BASE_URL}/validity",
        headers={"Authorization": f"Bearer {invalid_jwt}"},
    )

    assert response.status_code == 401


def test_destroy_ticket_successfully(client, mocker):
    mock_braintree_gateway(mocker)

    response = client.post(TICKET_BASE_URL, json=valid_sale_data)
    response = client.put(
        f"{TICKET_BASE_URL}/destruction",
        headers=make_auth_header(response),
    )

    assert response.status_code == 200
