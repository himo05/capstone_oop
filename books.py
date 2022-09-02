class Author:  # create author class
    def __init__(self, name):  # initializer that sets parameters or arguments  
        self.name = name
        self.books = []  # empty books list

    def publish(self, title):
        if title in self.books:
            print(f'{title} is already in books list')
        else:
            self.books.append(title)
            

    def __str__(self):
        if self.books:
            book_list = ', '.join(self.books)
        else:
            book_list = 'No books'
        return f'Name: {self.name}. Books Published: {book_list}'

        
def main():
    shakespeare = Author('William Shakespeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Richard III')
    shakespeare.publish('Hamlet')


    print(shakespeare)

    himo = Author('Himo')
    print(himo)

main()