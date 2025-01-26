class Book:
    def __init__(self, title, author):
        """Constructor to initialize a Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Constructor to initialize an EBook instance with title, author, and file size."""
        super().__init__(title, author)  # Call the constructor of the base class (Book)
        self.file_size = file_size

    def __str__(self):
        """String representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Constructor to initialize a PrintBook instance with title, author, and page count."""
        super().__init__(title, author)  # Call the constructor of the base class (Book)
        self.page_count = page_count

    def __str__(self):
        """String representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Constructor to initialize a Library instance with an empty book collection."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print the details of all books in the library."""
        for book in self.books:
            print(book)
