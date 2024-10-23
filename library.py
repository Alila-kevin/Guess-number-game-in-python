class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
    
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Not Available'}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
    
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def list_books(self):
        for book in self.books:
            print(book)

# Example usage
if __name__ == "__main__":
    library = Library("City Library")
    
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    
    library.add_book(book1)
    library.add_book(book2)
    
    print("Books in the library:")
    library.list_books()
    
    print("\nFinding book with ISBN 1234567890:")
    found_book = library.find_book("1234567890")
    print(found_book)
    
    print("\nRemoving book with ISBN 0987654321.")
    library.remove_book("0987654321")
    
    print("\nBooks in the library after removal:")
    library.list_books()
