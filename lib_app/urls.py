from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lib_app import views
from lib_app.api_views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'author', AuthorViewSet, basename='author'),
router.register(r'book', BookViewSet, basename='book'),

urlpatterns = [
    path('', views.login_view, name='login1'),
    path('base', views.admin_view, name="base"),
    path('', include(router.urls)),#for_rest_api
    path('viewauthorlist', views.viewAuthorList, name="viewauthorlist"),
    path('viewbooklist', views.viewBookList, name="viewbooklist"),
    path('updateAuthorDetails<int:id>', views.updateAuthorDetails, name="updateAuthorDetails"),
    path('updateBookDetails<int:id>', views.updateBookDetails, name="updateBookDetails"),
    path('viewAuthorDetails<int:id>', views.viewAuthorDetails, name="viewAuthorDetails"),
    path('search_authors', views.search_authors, name="search_authors"),
    path('search_books', views.search_books, name="search_books")


]
