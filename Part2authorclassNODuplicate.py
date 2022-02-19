class Author:
    def __init__(self, name):
        self.name = name
        self.books = [] #Created empty list

    def publish(self, title):  # funtion for the publishing book
        #if the book is in the list it will return a message saying its already there
        if title in self.books:
            print('Sorry, that book has already been added to the author\'s list.')
        else:  #else add the book with no duplicate of the author
            self.books.append(title)

    def __str__(self):
        titles = ', '.join( #this will join the book that is going to be published
            self.books) or 'This Author Has No Published Books'
        return f'Name: {self.name} | Books Published: {titles}'


def main():
    shakespeare = Author('William Shakespeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Richard III')
    print(shakespeare)

    mina = Author('Mina')
    print(mina)


if __name__ == '__main__':
    main()