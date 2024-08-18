class Category:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.SubcategoryList = []
    
    def __str__(self):
        return f"{self.code} ({self.name})"

class Subcategory:
    def __init__(self, category, name):
        self.name = name
        self.category = category
        self.AuthorBookList = []
        for i in self.category.SubcategoryList:
            if i.name == self.name:
                self.code = i.code
                break
        else:
            category.SubcategoryList.append(self)
            self.code = f"{self.category.code} {len(self.category.SubcategoryList) - 1}"

    def __str__(self):
        return f"{self.code} ({self.name})"

class Book:
    def __init__(self, name, author, subcategory, publisher, year, volume=1):
        self.name = name
        self.author = author
        self.subcategory = subcategory
        self.publisher = publisher
        self.year = year
        self.volume = volume
        self.copy = 1

        self.authorCode = len(self.subcategory.AuthorBookList) + 1
        self.bookCode = 1

        for i in self.subcategory.AuthorBookList:
            if self.author in i:
                author_books = i[self.author]
                self.authorCode = self.subcategory.AuthorBookList.index(i) + 1
                for book in author_books:
                    if book.name == self.name and book.publisher == self.publisher and book.year == self.year and book.volume == self.volume:
                        book.copy += 1
                        self.copy = book.copy
                        self.bookCode = author_books.index(book) + 1
                        break
                else:
                    author_books.append(self)
                    self.bookCode = len(author_books)
                break
        else:
            self.subcategory.AuthorBookList.append({self.author: [self]})
        
    def __str__(self):
        return f"{self.subcategory.code}. {self.authorCode} {self.bookCode}"

# Creating a Category
fiction_category = Category(code="FIC", name="Fiction")

# Creating Subcategories
mystery_subcategory = Subcategory(category=fiction_category, name="Mystery")
fantasy_subcategory = Subcategory(category=fiction_category, name="Fantasy")

# Adding Books to Subcategories
book1 = Book(name="The Hound of the Baskervilles", author="Arthur Conan Doyle", subcategory=mystery_subcategory, publisher="Penguin Classics", year=1902)
book2 = Book(name="The Sign of the Four", author="Arthur Conan Doyle", subcategory=mystery_subcategory, publisher="Penguin Classics", year=1890)
book3 = Book(name="Harry Potter and the Sorcerer's Stone", author="J.K. Rowling", subcategory=fantasy_subcategory, publisher="Bloomsbury", year=1997)

# Adding a Duplicate Book to Test Copy Increment
book4 = Book(name="Harry Potter and the Sorcerer's Stone", author="J.K. Rowling", subcategory=fantasy_subcategory, publisher="Bloomsbury", year=1997)

# Printing Category, Subcategory, and Book Codes
print(fiction_category)  # Output: FIC (Fiction)
print(mystery_subcategory)  # Output: FIC 0 (Mystery)
print(fantasy_subcategory)  # Output: FIC 1 (Fantasy)

print(book1)  # Output: FIC 0. 1 1 (Arthur Conan Doyle's first book in Mystery)
print(book2)  # Output: FIC 0. 1 2 (Arthur Conan Doyle's second book in Mystery)
print(book3)  # Output: FIC 1. 1 1 (J.K. Rowling's first book in Fantasy)
print(book4)  # Output: FIC 1. 1 1 (Same as above, but the copy count increments)
