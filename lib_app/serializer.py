from rest_framework import serializers

from lib_app.models import Author, Book


class Author_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_name', 'username', 'email',)

class Book_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_name', 'author_name', 'created_date',)
