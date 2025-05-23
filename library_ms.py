class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' has been added to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You've successfully borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print(f"Sorry, '{title}' is not in our library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"Thank you for returning '{book.title}'.")
                    return
                else:
                    print(f"'{book.title}' wasn't borrowed.")
                    return
        print(f"Sorry, '{title}' doesn't belong to this library.")

    def list_books(self):
        print(f"Books in {self.name}:")
        for book in self.books:
            print(book)
