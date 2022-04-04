from marshmallow import fields

from .base import BaseSchema


class ObjectSchema(BaseSchema):
    id = fields.Integer(required=True, dump_only=True)
    identifier = fields.String(required=True, dump_only=True)
    name = fields.String(required=True, dump_only=True)
    description_url = fields.String(required=True, dump_only=True)
