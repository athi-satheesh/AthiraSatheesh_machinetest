# Generated by Django 5.0.1 on 2024-01-26 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='lib_app.author')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookid', to='lib_app.book')),
                ('book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookname', to='lib_app.book')),
                ('created_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='date', to='lib_app.book')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_email', to='lib_app.author')),
                ('phone_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phoneNo', to='lib_app.author')),
            ],
        ),
    ]