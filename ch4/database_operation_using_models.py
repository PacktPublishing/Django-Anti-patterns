from myapp.models import Book

# Create a new book
new_book = Book(title="Sample Book", author="John Doe", publication_date="2024-05-12")
new_book.save()

# Retrieve all books
all_books = Book.objects.all()

# Update a book
book_to_update = Book.objects.get(title="Sample Book")
book_to_update.author = "Jane Smith"
book_to_update.save()

# Delete a book
book_to_delete = Book.objects.get(title="Sample Book")
book_to_delete.delete()
