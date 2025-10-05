# book_library.py

class Book:
    def __init__(self, title, author):
        self.title = title           # public
        self.author = author         # public
        self._is_checked_out = False # private

    def check_out(self):
        """Marks the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # already checked out

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # wasn't checked out

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list to store Book objects

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def check_out_book(self, title):
        """Find and check out a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"You checked out '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """Find and return a checked-out book."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"'{book.title}' has been returned.")
                    return
                else:
                    print(f"'{book.title}' was not checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """List all books that are currently available."""
        available = [book for book in self._books if book.is_available()]
        if available:
            print("\nAvailable Books:")
            for book in available:
                print(f" - {book.title} by {book.author}")
        else:
            print("No books are currently available.")
