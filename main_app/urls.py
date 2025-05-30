from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import BookViewSet, BookCustomViewSet, ActionViewSet, PizzaCustomeViewSet
from .views import PizzaCustomeViewSet
from .views import confirm_book

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
router.register('custom_books', BookCustomViewSet, basename="custom_book")
router.register('common_elements', ActionViewSet, basename="common_elements")
router.register('pizza', PizzaCustomeViewSet, basename="pizza")

urlpatterns = [
    # path("", views.home, name="home"),
    # path("second", views.second, name="second"),
    # path("get_data", views.get_data, name="get_data"),
    # path("api/books", views.get_books, name="get_books"),
    # path("books", views.get_books_page, name="books_page")
    path("", include(router.urls)),
    # path("main/", views.home, name="home"),
    path('home/', views.home, name='home'),
    path("books/add/", views.add_book, name="add_book"),
    path("books/", views.my_books, name="my_books"),
    path("books/delete/<int:book_id>/", views.delete_book, name="delete_book"),
    path("books/confirm_delete/<int:book_id>/", confirm_book, name="confirm_book"),
    path('users/', views.get_users, name='get_users'),
    path('books/by_user/<int:user_id>/', views.books_by_user, name='books_by_user'),

]

