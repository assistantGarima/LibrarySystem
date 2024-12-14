class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    def add_book(self, book_title, quantity=1):
        """Add a book to the library."""
        if book_title in self.books:
            self.books[book_title] += quantity
        else:
            self.books[book_title] = quantity
        print(f'Added "{book_title}" ({quantity} copies) to the library.')

    def view_books(self):
        """View all available books in the library."""
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book, quantity in self.books.items():
                print(f'- {book}: {quantity} copies')

    def borrow_book(self, user, book_title):
        """Borrow a book from the library."""
        if book_title not in self.books or self.books[book_title] == 0:
            print(f'Sorry, "{book_title}" is not available.')
            return

        # Deduct one copy of the book
        self.books[book_title] -= 1
        if user not in self.borrowed_books:
            self.borrowed_books[user] = []
        self.borrowed_books[user].append(book_title)
        print(f'"{book_title}" has been borrowed by {user}.')

    def return_book(self, user, book_title):
        """Return a book to the library."""
        if user not in self.borrowed_books or book_title not in self.borrowed_books[user]:
            print(f'{user} has not borrowed "{book_title}".')
            return

        # Increment the book quantity in the library
        self.books[book_title] += 1
        self.borrowed_books[user].remove(book_title)
        print(f'"{book_title}" has been returned by {user}.')

        # Remove user from borrowed_books if they have no books
        if not self.borrowed_books[user]:
            del self.borrowed_books[user]

    def view_borrowed_books(self):
        """View all borrowed books."""
        if not self.borrowed_books:
            print("No books are currently borrowed.")
        else:
            print("Borrowed books:")
            for user, books in self.borrowed_books.items():
                print(f'{user} has borrowed: {", ".join(books)}')


# Sample Usage
library = Library()

# Adding books to the library
library.add_book("Python Programming", 5)
library.add_book("Data Science Basics", 3)

# Viewing books
library.view_books()

# Borrowing books
library.borrow_book("Alice", "Python Programming")
library.borrow_book("Bob", "Data Science Basics")

# Viewing borrowed books
library.view_borrowed_books()

# Returning books
library.return_book("Alice", "Python Programming")

# Viewing books after return
library.view_books()
library.view_borrowed_books()
