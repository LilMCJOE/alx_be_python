 #
 # Creating Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def checkout(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_checked_out(self):
        return self._is_checked_out

# Creating Library Class

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.checkout()
                print(f"Checked out: {book.title} by {book.author}")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                print(f"Returned: {book.title} by {book.author}")
                return
        print(f"Book '{title}' cannot be returned as it is not checked out or does not exist.")

    def list_available_books(self):
        print("Available books:")
        for book in self._books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}") 


