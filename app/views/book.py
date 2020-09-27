from flask import request
from flask_restplus import Resource
from app.restplus import api
from app.config import db
from app.models.book import Book
from app.serializers.book import book_serializer
from app.schemas.book import BookSchema

ns_book = api.namespace('book')

@ns_book.route('/')
class BookView(Resource):

    def get(self):
        books = Book.query.all()
        result = BookSchema(many=True).dump(books)

        return result, 200

    @ns_book.expect(book_serializer)
    def post(self):
        title = request.json['title']
        description = request.json['description']
        author_id = request.json['author_id']
        book = Book(title, description, author_id)
        db.session.add(book)
        db.session.commit()
        result = BookSchema().dump(book)

        return result, 201

@ns_book.route('/<id>')
class BookViewId(Resource):

    def get(self, id):
        book = Book.query.get(id)
        result = BookSchema().dump(book)

        return result, 200

    @ns_book.expect(book_serializer)
    def put(self, id):
        book = Book.query.get(id)
        title = request.json['title']
        description = request.json['description']
        author_id = request.json['author_id']
        book.title = title
        book.description = description
        book.author_id = author_id
        db.session.commit()
        result = BookSchema().dump(book)

        return result, 201

    def delete(self, id):
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()
        result = BookSchema().dump(book)

        return result, 202