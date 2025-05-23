# Generated by Django 5.1.7 on 2025-05-24 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_book_chapter_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(blank=True)),
                ('published', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='main_app.book')),
            ],
        ),
    ]
