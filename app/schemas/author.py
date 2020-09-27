from app.config import ma
from app.models.author import Author

class AuthorSchema(ma.Schema):
    class Meta:
        model = Author

    name = ma.Str(required=True)