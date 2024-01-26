from django.contrib import admin

from lib_app import models

# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Book)