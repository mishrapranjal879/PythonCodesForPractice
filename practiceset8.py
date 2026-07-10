# Project-------

# Library Management System (OOP Project)----


# Book Class
class Book:

    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    # Display Book Details
    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title      : {self.title}")
        print(f"Author     : {self.author}")
        print(f"Status     : {status}")
        print("-" * 35)


# Library Class
class Library:

    # Constructor
    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self):
        title = input("Enter Book Title : ")
        author = input("Enter Author Name : ")

        book = Book(title, author)
        self.books.append(book)

        print("\nBook Added Successfully!\n")

    # Display All Books
    def display_books(self):

        if len(self.books) == 0:
            print("\nNo Books Available!\n")
            return

        print("\n===== Library Books =====\n")

        for book in self.books:
            book.display()

    # Borrow Book
    def borrow_book(self):

        title = input("Enter Book Title to Borrow : ")

        for book in self.books:
            if book.title.lower() == title.lower():

                if book.available:
                    book.available = False
                    print("\nBook Borrowed Successfully!\n")
                else:
                    print("\nBook is Already Borrowed!\n")

                return

        print("\nBook Not Found!\n")

    # Return Book
    def return_book(self):

        title = input("Enter Book Title to Return : ")

        for book in self.books:

            if book.title.lower() == title.lower():

                if not book.available:
                    book.available = True
                    print("\nBook Returned Successfully!\n")
                else:
                    print("\nThis Book Was Not Borrowed!\n")

                return

        print("\nBook Not Found!\n")


# Main Program


library = Library()

while True:

    print("========== Library Management System ==========")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter Your Choice : ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        library.borrow_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        print("\nThank You for Using Library Management System!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.\n")