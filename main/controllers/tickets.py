import uuid

import braintree
from flask import jsonify

from main import app, config
from main.commons.decorators import require_not_expired_ticket, validate_request
from main.commons.exceptions import BadRequest
from main.engines import ticket as ticket_engine
from main.enums import HttpElement
from main.libs.jwt import create_access_token
from main.schemas.sale import SaleSchema


@app.post("/tickets")
@validate_request(HttpElement.BODY, SaleSchema())
def create_sale(data, **__):
    gateway = braintree.BraintreeGateway(
        braintree.Configuration(
            braintree.Environment.Sandbox,
            merchant_id=config.BRAINTREE_MERCHANT_ID,
            public_key=config.BRAINTREE_PUBLIC_KEY,
            private_key=config.BRAINTREE_PRIVATE_KEY,
        )
    )

    order_id = str(uuid.uuid4())
    result = gateway.transaction.sale(
        {
            "amount": data["amount"],
            "payment_method_nonce": data["nonce"],
            "device_data": data["device_data"],
            "order_id": order_id,
            "options": {
                "submit_for_settlement": True,
                "paypal": {
                    "custom_field": "PayPal custom field",
                    "description": "Description for PayPal email receipt",
                },
            },
        }
    )

    if not result.is_success:
        raise BadRequest(error_message="Unable to make a payment.")

    ticket = ticket_engine.create_ticket(result.transaction.id)

    return jsonify(access_token=create_access_token(ticket.id))


@app.put("/tickets/destruction")
@require_not_expired_ticket
def destroy_ticket(ticket):
    ticket_engine.destroy_ticket(ticket)
    return jsonify({})


@app.get("/tickets/validity")
@require_not_expired_ticket
def validate_ticket(**__):
    return jsonify({})
