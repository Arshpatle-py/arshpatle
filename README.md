# Class for Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("----------------------")


# Class for Patron
class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print("-", book.title)
        else:
            print("No books borrowed.")
        print("----------------------")


# Class for Library
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add book
    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" added to the library.')

    # Register patron
    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f'Patron "{patron.name}" registered successfully.')

    # Issue book
    def issue_book(self, title, patron_name):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    for patron in self.patrons:
                        if patron.name.lower() == patron_name.lower():
                            book.available = False
                            patron.borrowed_books.append(book)
                            print(f'"{book.title}" issued to {patron.name}.')
                            return
                    print("Patron not found.")
                    return
                else:
                    print("Book is already issued.")
                    return
        print("Book not found.")

    # Return book
    def return_book(self, title, patron_name):
        for patron in self.patrons:
            if patron.name.lower() == patron_name.lower():
                for book in patron.borrowed_books:
                    if book.title.lower() == title.lower():
                        book.available = True
                        patron.borrowed_books.remove(book)
                        print(f'"{book.title}" returned successfully.')
                        return
        print("Return failed. Book or Patron not found.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        print("======================")
        for book in self.books:
            book.display()


# ---------------- MAIN PROGRAM ----------------

library = Library()

# Adding two books
book1 = Book("Python Programming", "John Zelle")
book2 = Book("The Alchemist", "Paulo Coelho")

library.add_book(book1)
library.add_book(book2)

# Registering a patron
patron1 = Patron("Arsh Patle")
library.register_patron(patron1)

# Display books
library.display_books()

# Issue a book
library.issue_book("Python Programming", "Arsh Patle")

# Display books after issuing
library.display_books()

# Display patron details
patron1.display()

# Return the book
library.return_book("Python Programming", "Arsh Patle")

# Display books after return
library.display_books()

# Display patron details again
patron1.display()
