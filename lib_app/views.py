from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from lib_app.forms import Author_listForm, Book_listForm
from lib_app.models import Author, Book, AuthorDetails
from lib_app.serializer import Author_listSerializer, Book_listSerializer


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('base')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, "Admin_Login.html")


# getting_admin_view_after_login
def admin_view(request):
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    return render(request, "index_admin.html", {'total_authors_count': total_authors_count, 'total_books_count': total_books_count})


class Author_list(APIView):
    def get(self, request):
        author_data = Author.objects.all()
        serializer = Author_listSerializer(author_data, many=True)
        return Response(serializer.data)


class Book_list(APIView):
    def get(self, request):
        book_data = Book.objects.all()
        serializer = Book_listSerializer(book_data, many=True)
        return Response(serializer.data)


def viewAuthorList(request):
    data = Author.objects.all()
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    addAuthor_form = Author_listForm()
    per_page = 10

    paginator = Paginator(data, per_page)
    page = request.GET.get('page')

    try:
        authors = paginator.page(page)
    except PageNotAnInteger:
        authors = paginator.page(1)
    except EmptyPage:
        authors = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        addAuthor_form = Author_listForm(request.POST)
        if 'submit' in request.POST:
            addAuthor_form1 = Author_listForm(request.POST)
            if addAuthor_form1.is_valid():
                addAuthor_form1.save()
                return redirect('viewauthorlist')
        elif 'cancel' in request.POST:
            return redirect('viewauthorlist')

    return render(request, 'view_authorList.html', {'data': data, 'authors': authors, 'author_form': addAuthor_form, 'total_authors_count': total_authors_count, 'total_books_count': total_books_count})


def viewBookList(request):
    data = Book.objects.all()
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    addBook_form = Book_listForm()
    per_page = 10

    paginator = Paginator(data, per_page)
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        addBook_form = Book_listForm(request.POST)
        if 'submit' in request.POST:
            addBook_form1 = Book_listForm(request.POST)
            if addBook_form1.is_valid():
                addBook_form1.save()
                return redirect('viewbooklist')
        elif 'cancel' in request.POST:
            return redirect('viewbooklist')

    return render(request, 'view_bookList.html', {'data': data, 'books': books, 'book_form': addBook_form, 'total_books_count': total_books_count, 'total_authors_count': total_authors_count})


def updateAuthorDetails(request, id):
    author_data = Author.objects.get(id=id)
    addAuthor_form = Author_listForm(instance=author_data)
    if request.method == "POST":
        addAuthor_form1 = Author_listForm(request.POST, instance=author_data)
        if addAuthor_form1.is_valid():
            addAuthor_form1.save()
            return redirect('viewauthorlist')
    return render(request, "updateAuthorDetails.html", {'Author_form': addAuthor_form})


def viewAuthorDetails(request, id):
    author_details = AuthorDetails.objects.get(id=id)
    return render(request, 'viewAuthorDetails.html', {'author_details': author_details})


def search_authors(request):
    query = request.GET.get('q')  # Get the query parameter from the URL
    authors = Author.objects.all()
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    if query:
        # If a query is provided, filter authors based on the name containing the query
        authors = authors.filter(author_name__icontains=query)
    return render(request, 'search_authors.html', {'authors': authors, 'query': query, 'total_books_count': total_books_count, 'total_authors_count': total_authors_count})


def search_books(request):
    query = request.GET.get('q')  # Get the query parameter from the URL
    books = Book.objects.all()
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    if query:
        # If a query is provided, filter authors based on the name containing the query
        books = books.filter(book_name__icontains=query)
    return render(request, 'search_book.html', {'books': books, 'query': query, 'total_books_count': total_books_count, 'total_authors_count': total_authors_count})
