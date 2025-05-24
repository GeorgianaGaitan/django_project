import pytest
from django.contrib.auth import get_user_model
from main_app.models import Book
@pytest.mark.django_db
def test_create_book():
    user = get_user_model().objects.create_user(username="user1", password="password12345")
    #assert len(get_user_model().objects.all()) == 1
    book = Book.objects.create(title="Title", author= "Max", page_count=3, created_by=user)
    assert book.title == "Title"
    assert book.author == "Max"
    assert book.page_count == 3
    assert book.created_by == user
