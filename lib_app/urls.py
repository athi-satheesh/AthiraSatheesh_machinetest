from django.urls import path

from lib_app import views

urlpatterns = [
    path('', views.login_view, name='login1'),
    path('base', views.admin_view, name="base"),
    path('authorlist', views.Author_list.as_view(), name="authorlist"),
    path('booklist', views.Book_list.as_view(), name="booklist"),
    path('viewauthorlist', views.viewAuthorList, name="viewauthorlist"),
    path('viewbooklist', views.viewBookList, name="viewbooklist"),
    path('updateAuthorDetails<int:id>', views.updateAuthorDetails, name="updateAuthorDetails"),
    path('viewAuthorDetails<int:id>', views.viewAuthorList, name="viewAuthorDetails"),
    path('search_authors', views.search_authors, name="search_authors"),
    path('search_books', views.search_books, name="search_books")


]
