import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()
from main_app.models import Book
from main_app.utils import create_book_detail



def run():
    book = Book.objects.all()[0]
    for book in books:
        try:
            print(book.detail)
        except Exception as e:
            create_book_detail(book)
            print("Created book detail, for book:")
            print(book)

if __name__ == '__main__':
    run()