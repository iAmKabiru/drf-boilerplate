from rest_framework.serializers import ModelSerializer
from .models import User, Book

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
        

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'author', 'isbn')