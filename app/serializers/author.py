from app.restplus import api
from flask_restplus import fields

author_serializer = api.model('Author', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True)
})