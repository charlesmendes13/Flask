from app.config import ma
from app.models.book import Book

class BookSchema(ma.Schema):
    class Meta:
        model = Book

    title = ma.Str(required=True)
    description = ma.Str(required=True)
    author = ma.Nested("AuthorSchema")