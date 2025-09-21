from marshmallow import Schema, fields, validate

from config import Config


class XirrCalculationRequestSchema(Schema):
    dates = fields.List(fields.Date(Config.DATE_FORMAT), required=True, validate=[validate.Length(min=2)])
    cashflows = fields.List(fields.Float(), required=True, validate=[validate.Length(min=2)])
