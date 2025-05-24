#fixture
from base64 import decode
from quopri import decodestring
from urllib import response

import pytest

from django.contrib.auth.models import User
from django.db import models
from django.template.context_processors import request
from django.test import Client
from django.urls import reverse
from main_app import models



@pytest.fixture

def user(db):
    return User.objects.create_user(username='Ala', password='test1234')
@pytest.fixture
def client_logged_in(client, user):
    client.login(username='Ala', password='test1234')
    v = 10
    v = "asdf"

    return client

@pytest.fixture
def book(user):
    list1 = []
    list1.append(Book.objects.create(title='test1', author='test author', page_count= 301, created_by=user))
    list1.append(Book.objects.create(title='test1', author='test author', page_count=300, created_by=user))
    return list1


def test_books_custom_view(client_logged_in, user):
    client_logged_in.get(reverse("/custom_book/"))
    assert response.status_code == 200
    assert response.data is not None
    assertlen(response.data) == 3
    assert user is not None

    response_single_get = client_logged_in.get("/custom_books/1/")
    response_single_get.data.serializer.instance
    Book(title="Test1",author="Test Author")
    assert response_single_get.response.status_code == 200
    assert book.title == book_instance.title
    assert book.title == book_instance.title
    assert book.author == book_instance.author
    assert book_instance.created_by == user
    assert book == book_instance

    response_get_wrong = client_logged_in.get("/custom_books/200/")
    assert response_get_wrong.status_code == 404
    assert "Book not found!" in response_get_wrong.content.decode()

    response_deleted = client_logged_in.get("/custom_books/delete/3/")
    assert response_deleted.status_code == 200
    assert "book deleted!" in response_deleted.content.decode()


    book_data_to_created = {
        "title":"Test Created 1",
        "author": "test creator1",
        "page_count":301,
        "created_by":user.id
    }
    response_created = client_logged_in.get("/custom_books/create/", book_data_to_created)
    assert response_created.status_code == 201
    assert "book created!" in response_created.content.decode()
    assert Book.objects.filter(title="test created 1").exist()

def test_my_books(client_logged_in, user):
    response = client_logged_in.get("/books/")
    decoded =  response.content.decode()
    assert response.status_code == 200
    assert book.titlw in decoded
    assert book[0].title in decoded
    assert book[1].title in decoded

    print(response)


def test_add_book_view(client_logged_in, user,book,books):
    url = "/books/add/"
    response = client_logged_in.get(url)
    decoded = response.content.decode()
    assert response.status_code == 200
    assert "Add a new book" in decoded

    template_list = [t for t in response.templates]
    assert "add_book.html" in template_list

def test_confirm_delete(client_logged_in,user, book):
   url = "/book/confirm_delete/1/"
   assert response.status_code == 200
   assert "Are you sure?" in decoded
   assert book.title in decoded

   response = client_logged_in.post("/books/delete/1/")
   assert response.status_code == 200
   assert len(Book.objects.all()) == 0


def test_get_all_users(db, client:client.Client):
    User.objects.create_user(username="Ala", password='test1234')
    User.objects.create_user(username='Andrei', password='test1234234')
    url = "/users/"
    response = client.get(url)
    response = response.content.decode()
    asssert "Ala" in response
def test_get_books_by_user(db, client;Client, books, user):
    user_id = user.id

    url = "/users/{}/books/".format(user_id)
    response = response.content.decode()