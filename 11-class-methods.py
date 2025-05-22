class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()
    def display_info(self): 
        print(f"Title: {self.title}, Author: {self.author}")
    @classmethod
    def display_total_books(cls):
        print(f"Total books: {cls.total_books}")
# Create instances of Book
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
# Display information about each book
book1.display_info()  # Output: Title: 1984, Author: George Orwell
book2.display_info()  # Output: Title: To Kill a Mockingbird, Author: Harper Lee
book3.display_info()  # Output: Title: The Great Gatsby, Author: F. Scott Fitzgerald
# Display the total number of books created
Book.display_total_books()  # Output: Total books: 3
# The Book class has a class variable total_books that keeps track of the total number of books created.
# The increment_book_count class method is called in the constructor to update the count whenever a new book instance is created.
