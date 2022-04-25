from marshmallow import fields

from .base import BaseSchema


class SaleSchema(BaseSchema):
    amount = fields.String(required=True, load_only=True)
    nonce = fields.String(required=True, load_only=True)
    device_data = fields.String(required=True, load_only=True)
