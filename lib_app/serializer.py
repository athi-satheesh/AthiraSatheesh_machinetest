from rest_framework import serializers

from lib_app.models import Author, Book


#Creating serializer for listing out authors
class Author_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_name', 'username', 'email',)

#Creating serializer for listing out books
class Book_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_name', 'author_name', 'created_date',)
