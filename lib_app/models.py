from django.db import models


# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_id = models.CharField(max_length=10)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    created_date = models.DateField()

    def __str__(self):
        return self.book_name


class AuthorDetails(models.Model):
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='name')
    email = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_email')
    phone_number = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='phoneNo')
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='bookname')
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='bookid')
    created_date = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='date')
