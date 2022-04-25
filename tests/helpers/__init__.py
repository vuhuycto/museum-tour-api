from flask import Response

OBJECT_BASE_URL = "/objects"
TICKET_BASE_URL = "/tickets"


valid_sale_data = {"amount": "1", "nonce": "a", "device_data": "a"}
invalid_sale_data = {"amount": "1", "nonce": "a"}

invalid_jwt = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MX0."
    "-xXA0iKB4mVNvWLYFtt2xNiYkFpObF54J9lj2RwduA"
)


def make_auth_header(response: Response):
    return {"Authorization": f"Bearer {response.json['access_token']}"}
