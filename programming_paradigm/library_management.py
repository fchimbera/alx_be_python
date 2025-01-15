class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False

    def is_checked_out(self):
        return self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                #return f"{title} has been checked out."
        #return "Book is unavailable, check book listings."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                #return f"{title} has been returned."
        ##return "Book was not checked out."

    def list_available_books(self):
        for book in self._books:
            if not book.is_checked_out():
                print(f"{book.title} by {book.author}")
