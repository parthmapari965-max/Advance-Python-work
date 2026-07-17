"""
Library Management System

Problem Statement:
 The system should maintain information about
books and library patrons. It must provide functionalities
to add new books, register patrons, issue books to
patrons, and accept returned books. The program
should efficiently track the availability of books and the
borrowing records of patrons using appropriate classes
and objects.
"""

# Book Class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)

        if self.available:
            print("Status  : Available")
        else:
            print("Status  : Issued")

        print("----------------------------")


# Patron Class
class Patron:
    def __init__(self, patron_id, name, phone):
        self.patron_id = patron_id
        self.name = name
        self.phone = phone

    def display(self):
        print("Patron ID :", self.patron_id)
        print("Name      :", self.name)
        print("Phone     :", self.phone)
        print("----------------------------")


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add a new book
    def add_book(self, book):
        self.books.append(book)
        print(book.title, "added successfully.")

    # Register a new patron
    def register_patron(self, patron):
        self.patrons.append(patron)
        print(patron.name, "registered successfully.")

    # Issue a book
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return

        print("Book not found.")

    # Return a book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print("Book returned successfully.")
                else:
                    print("This book was not issued.")
                return

        print("Book not found.")

    # Display all books
    def show_books(self):
        print("\nLibrary Books")
        print("======================")
        for book in self.books:
            book.display()


# ---------------- Main Program ----------------

library = Library()

# Create Books
book1 = Book(101, "The 48 Laws of Power", "Robert Greene")
book2 = Book(102, "The Art of Seduction", "Robert Greene")

# Add Books
library.add_book(book1)
library.add_book(book2)

# Create Patron
patron1 = Patron(1, "Ansh", "9876543210")

# Register Patron
library.register_patron(patron1)

# Display Books
library.show_books()

# Issue Book
library.issue_book(101)

# Display Books Again
library.show_books()

# Return Book
library.return_book(101)

# Display Final Status
library.show_books()