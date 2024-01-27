import datetime

from django.contrib.auth import forms
from django import forms

from lib_app.models import Author, Book


class DateInput(forms.DateInput):
    input_type = 'date'


# to_display_and_add_authors
class Author_listForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('author_name', 'username', 'email', 'phone_no')


# to_display_and_add_books
class Book_listForm(forms.ModelForm):
    created_date = forms.DateField(widget=DateInput)

    def clean_date(self):
        created_date = self.cleaned_data['dob']
        if created_date > datetime.date.today():
            raise forms.ValidationError("The date cannot be in future!")
        return created_date

    class Meta:
        model = Book
        fields = ('book_name', 'book_id', 'author_name', 'created_date',)


# to_display_books_of_a_specific_author(Detailed View of Author)
class Bookform_for_specificAuthor(forms.ModelForm):
    created_date = forms.DateField(widget=DateInput)

    def clean_date(self):
        created_date = self.cleaned_data['dob']
        if created_date > datetime.date.today():
            raise forms.ValidationError("The date cannot be in future!")
        return created_date

    class Meta:
        model = Book
        fields = ('book_name', 'author_name', 'book_id', 'created_date',)

        def __init__(self, *args, **kwargs):
            super(Bookform_for_specificAuthor, self).__init__(*args, **kwargs)
            self.fields['author_name'].widget.attrs['readonly'] = True
