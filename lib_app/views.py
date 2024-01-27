from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from lib_app.forms import Author_listForm, Book_listForm, Bookform_for_specificAuthor
from lib_app.models import Author, Book


# Creating Login view for User
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


# Getting admin view after Admin Login
def admin_view(request):
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    return render(request, "index_admin.html", {'total_authors_count': total_authors_count, 'total_books_count': total_books_count})


# To display the list of Authors by function-based
def viewAuthorList(request):
    author_list = Author.objects.all().order_by('author_name')
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    addAuthor_form = Author_listForm()
    #Adding pagination with 10 records per page
    per_page = 10
    paginator = Paginator(author_list, per_page)
    page = request.GET.get('page')
    try:
        authors = paginator.page(page)
    except PageNotAnInteger:
        authors = paginator.page(1)
    except EmptyPage:
        authors = paginator.page(paginator.num_pages)
    #Adding new Author and validating if it already exists or not.
    if request.method == 'POST':
        addAuthor_form = Author_listForm(request.POST)
        if 'submit' in request.POST:
            addAuthor_form1 = Author_listForm(request.POST)
            if addAuthor_form1.is_valid():
                authorname = addAuthor_form1.cleaned_data['author_name']
                if not Author.objects.filter(author_name=authorname).exists():
                    addAuthor_form1.save()
                    return redirect('viewauthorlist')
                else:
                    messages.info(request, 'Author already Added')
        elif 'cancel' in request.POST:
            return redirect('viewauthorlist')

    return render(request, 'view_authorList.html', {'authors': authors, 'author_form': addAuthor_form, 'total_authors_count': total_authors_count, 'total_books_count': total_books_count})


# To display the list of Books by function-based
def viewBookList(request):
    book_list = Book.objects.all().order_by('book_name')
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    addBook_form = Book_listForm()
    # Adding pagination with 10 records per page
    per_page = 10
    paginator = Paginator(book_list, per_page)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    # Adding new Book and validating if it already exists or not.
    if request.method == 'POST':
        addBook_form = Book_listForm(request.POST)
        if 'submit' in request.POST:
            addBook_form1 = Book_listForm(request.POST)
            if addBook_form1.is_valid():
                bookname = addBook_form1.cleaned_data['book_name']
                authorname = addBook_form1.cleaned_data['author_name']
                if not Book.objects.filter(book_name=bookname,author_name=authorname ).exists() :
                    addBook_form1.save()
                    return redirect('viewbooklist')
                else:
                    messages.info(request, 'Book already Added')
        elif 'cancel' in request.POST:
            return redirect('viewbooklist')

    return render(request, 'view_bookList.html', {'books': books, 'book_form': addBook_form, 'total_books_count': total_books_count, 'total_authors_count': total_authors_count})

#To update the details of existing author
def updateAuthorDetails(request, id):
    author_data = Author.objects.get(id=id)
    addAuthor_form = Author_listForm(instance=author_data)
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    if request.method == "POST":
        addAuthor_form1 = Author_listForm(request.POST, instance=author_data)
        if addAuthor_form1.is_valid():
            addAuthor_form1.save()
            return redirect('viewauthorlist')
    return render(request, "updateAuthorDetails.html", {'Author_form': addAuthor_form, 'total_books_count': total_books_count, 'total_authors_count': total_authors_count})

#To update details of already existing book
def updateBookDetails(request, id):
    book_data = Book.objects.get(id=id)
    addbook_form = Book_listForm(instance=book_data)
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    if request.method == "POST":
        addbook_form1 = Book_listForm(request.POST, instance=book_data)
        if addbook_form1.is_valid():
            addbook_form1.save()
            return redirect('viewbooklist')
    return render(request, "updateBookDetails.html", {'Book_form': addbook_form, 'total_books_count': total_books_count, 'total_authors_count': total_authors_count})

#To have a detailed view of each author which only contains his/her book list
def viewAuthorDetails(request,id):
    user = Author.objects.get(id=id)
    author_details = Author.objects.filter(author_name=user)
    books_by_author =  Book.objects.filter(author_name=user).order_by('book_name')
    addBook_form = Bookform_for_specificAuthor()
    if request.method == 'POST':
        addBook_form = Bookform_for_specificAuthor(request.POST)
        if 'submit' in request.POST:
            addBook_form1 = Bookform_for_specificAuthor(request.POST)
            if addBook_form1.is_valid():
                bookname = addBook_form1.cleaned_data['book_name']
                if not Book.objects.filter(book_name=bookname).exists():
                    addBook_form1.save()
                    return redirect('viewbooklist')
                else:
                    messages.info(request, 'Book already Added')
        elif 'cancel' in request.POST:
            return redirect('viewbooklist')

    return render(request, 'viewAuthorDetails.html', {'books_by_author': books_by_author, 'author_details': author_details, 'book_form':addBook_form})


#To search author using keywords of author name
def search_authors(request):
    query = request.GET.get('q')  # Getting the query parameter from the URL
    authors = Author.objects.all()
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    if query:
        # If a query is provided, filter authors based on the author name containing the query
        authors = authors.filter(author_name__icontains=query)
    return render(request, 'search_authors.html', {'authors': authors, 'query': query, 'total_books_count': total_books_count, 'total_authors_count': total_authors_count})

#To search books using keywords of book name
def search_books(request):
    query = request.GET.get('q')  # Getting the query parameter from the URL
    books = Book.objects.all()
    total_authors_count = Author.objects.count()
    total_books_count = Book.objects.count()
    if query:
        # If a query is provided, filter authors based on the book name containing the query
        books = books.filter(book_name__icontains=query)
    return render(request, 'search_book.html', {'books': books, 'query': query, 'total_books_count': total_books_count, 'total_authors_count': total_authors_count})
