from app.restplus import api
from flask_restplus import fields

book_serializer = api.model('Book', {
    'id': fields.Integer(readonly=True),
    'title': fields.String(required=True),
    'description': fields.String(required=True),
    'author_id': fields.Integer(required=True),
})