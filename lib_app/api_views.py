from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from lib_app.models import Author, Book
from lib_app.serializer import Author_listSerializer, Book_listSerializer


#To display list of authors using api  including keyword search
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = Author_listSerializer
    filter_backends = [SearchFilter]
    search_fields = ['author_name']

#To display list of books using api  including keyword search
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Book_listSerializer
    filter_backends = [SearchFilter]
    search_fields = ['book_name']
