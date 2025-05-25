#function to generate random isbn
#function to create a summary for input text
import random
from datetime import date
from .models import Book, BookDetail  # asigură-te că importurile sunt corecte

def generate_isbn():
    result = []
    for i in range(13):
        v = random.randint(0, 9)
        result.append(str(v))
    return ''.join(result)

def summarize_text(text):
    return text[:10]

def create_book_detail(book: Book):
    BookDetail.objects.create(
        book=book,
        summary=summarize_text(book.title),
        published_date=date.today(),
        isbn=generate_isbn()
    )


print(generate_isbn())
