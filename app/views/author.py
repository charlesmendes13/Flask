from flask import request
from flask_restplus import Resource
from app.restplus import api
from app.config import db
from app.models.author import Author
from app.serializers.author import author_serializer
from app.schemas.author import AuthorSchema

ns_author = api.namespace('author')

@ns_author.route('/')
class AuthorView(Resource):

    def get(self):
        authors = Author.query.all()
        result = AuthorSchema(many=True).dump(authors)

        return result, 200

    @ns_author.expect(author_serializer)
    def post(self):
        name = request.json['name']
        author = Author(name)
        db.session.add(author)
        db.session.commit()
        result = AuthorSchema().dump(author)

        return result, 201

@ns_author.route('/<id>')
class AuthorViewId(Resource):
    
    def get(self, id):
        author = Author.query.get(id)
        result = AuthorSchema().dump(author)

        return result, 200
    
    @ns_author.expect(author_serializer)
    def put(self, id):
        author = Author.query.get(id)
        name = request.json['name']
        author.name = name
        db.session.commit()
        result = AuthorSchema().dump(author)

        return result, 201
    
    def delete(self, id):
        author = Author.query.get(id)
        db.session.delete(author)
        db.session.commit()
        result = AuthorSchema().dump(author)

        return result, 202