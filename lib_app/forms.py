import datetime

from django.contrib.auth import forms
from django import forms

from lib_app.models import Author, Book, AuthorDetails


class DateInput(forms.DateInput):
    input_type = 'date'


class Author_listForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('author_name', 'username', 'email', 'phone_no')


class Book_listForm(forms.ModelForm):
    created_date = forms.DateField(widget=DateInput)

    def clean_date(self):
        created_date = self.cleaned_data['dob']
        if created_date > datetime.date.today():
            raise forms.ValidationError("The date cannot be in future!")
        return created_date

    class Meta:
        model = Book
        fields = ('book_name', 'author_name', 'created_date',)


class AuthorDetailForm(forms.ModelForm):
    class Meta:
        model = AuthorDetails
        fields = ('author_name', 'email', 'phone_number', 'book_name', 'book_id', 'created_date',)
