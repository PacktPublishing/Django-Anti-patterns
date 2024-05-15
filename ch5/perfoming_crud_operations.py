# Creating a new author
new_author = Author.objects.create(name='J.K. Rowling', birth_date='1965-07-31')

# Creating a new book associated with the author
new_book = Book.objects.create(title='Harry Potter and the Philosopher\'s Stone', publication_date='1997-06-26', author=new_author)

# Reading all books by a specific author
author_books = Book.objects.filter(author=new_author)

# Updating an existing book
book_to_update = Book.objects.get(title='Harry Potter and the Philosopher\'s Stone')
book_to_update.title = 'Harry Potter and the Sorcerer\'s Stone'
book_to_update.save()

# Deleting a book
book_to_delete = Book.objects.get(title='Harry Potter and the Sorcerer\'s Stone')
book_to_delete.delete()