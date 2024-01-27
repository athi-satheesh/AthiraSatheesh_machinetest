from django.db import models


#Creating model for Author
class Author(models.Model):
    author_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=100)
    status =models.CharField(default=True)

    def __str__(self):
        return self.author_name

#Creating model for Book
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_id = models.CharField(max_length=10)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    created_date = models.DateField()
    status = models.CharField(default=True)

    def __str__(self):
        return self.book_name



