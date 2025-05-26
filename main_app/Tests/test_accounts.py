import pytest
from django.contrib import get_user_model
from rest_framework.authtoken.admin import User
from accounts.models import UserLoginMetadata


@pytest.fixture
def user():
    return get_user_model().objects.create_user(username='test', password='1234')

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username='test', password='1234')
    assert user is None
    assert user.username == "user1"
    user = get_user_model().objects.create_user(username='test2', password='1234')
    assert len(get_user_model().objects.all()) == 2

def test_login_metadata_creation(user, client):
    client.login(username='test', password='123')
    metadata_list = UserLoginMetadata.objects.filter(user=user).delete()
    assert len(metadata_list) == 1

