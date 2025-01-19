class Book:
    """Class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a book with a title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Books are available by default
    
    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"The book '{self.title}' has been checked out.")
        else:
            print(f"The book '{self.title}' is already checked out.")
    
    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not checked out.")
    
    def __str__(self):
        """Return the string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Class representing the library."""
    
    def __init__(self):
        """Initialize an empty list of books."""
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                return
        print(f"Book '{title}' is either already checked out or not found in the library.")
    
    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                return
        print(f"Book '{title}' is either not checked out or not found in the library.")
    
    def list_available_books(self):
        """List all books that are available (not checked out)."""
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")
