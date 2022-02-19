##Part 1: Author class
# Create a new class called Author.
# An Author has a name, and a list of books published.
# When you create a new Author, they don't have any books. So create an empty books list attribute in the __init__ method.
# Your Author class should have a publish method, which takes the title of a book as an argument. Add the title of this book to this object's books list.
# Add a __str__ method that returns a String with the author's name, and the names of all of their book's titles.
# Write a main function to test your class, create some example authors, and publish some example books.
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def published(self, title):
        self.books.append(title)

    def __str__(self):
        if self.books:
            books_list = ', '.join(self.books)
        else:
            books_list = 'no books published! '
        return f'name:{self.name} books published : {books_list }'


shakespeare = Author('william shakespeare')
shakespeare.published('hamlet')
shakespeare.published('richard the third')
print(shakespeare)

