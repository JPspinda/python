class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.sharing = False
        
    
class Client:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.books = []

class Library:
    def __init__(self):
        self.clients = []
        self.books = []
        
    def adding_books(self):
        id = input("Report the book's ID: ")
        name = input("Report the book's name: ")
        author = input("Report the book's author: ")
        book = self.search_books(id)
        
        if book:
            print('ID already exists.')
            return
        else:
            self.books.append(Book(id, name, author))
            print("Your book was adding succesfully!")
        
    def adding_client(self):
        id = input("Report the client's ID: ")
        name = input("Report the client's name: ")
        age = input("Report the client's age: ")
        self.clients.append(Client(id, name, age))
        
    def listing_books(self):
        for book in self.books:
            print(book.id, book.name, book.author)
            
    def listing_clients(self):
        for client in self.clients:
            print(client.id, client.name, client.age, client.books)
            
    def search_books(self, id):
        for i in self.books:
            if i.id == id:
                return i
        return None        
            
    def search_client(self, id):
        for i in self.clients:
            if i.id == id:
                return i
        return None
        
    def share_book(self):
        book_id = input("Report the book's ID you wanto to share: ")    
        client_id = input("Report the client's ID you wanto to share the book: ")  
        
        book = self.search_books(book_id)  
        client = self.search_client(client_id)
        
        if not book:
            print('Book was not find.')
            return
        if not client:
            print('Client was not find.')
            return
        else:
            if book.sharing:
                print('This book has already been shared.')
                return
            else:
                book.sharing = True
                client.books.append(book.id)
    
    def delete_book(self):
        book_id = input("Report the book's ID you wanto to share: ")    
        client_id = input("Report the client's ID you wanto to share the book: ")  
        
        book = self.search_books(book_id)
        client = self.search_client(client_id)
        
        if not book:
            print('Book was not find.')
            return
        if not client:
            print('Client was not find.')
            return
        else:
            if not book.sharing:
                print('This book has already been shared.')
                return
            if book_id not in client.books:
                print('This book was not sharing to this client')
                return
            else:
                book.sharing = False
                client.books.remove(book_id)
            
    def listing_shared_books(self):
        client_id = input("Report the client's ID you wanto to share the book: ")
        
        client = self.search_client(client_id)
        for i in client.books:
            print(i)
        
l = Library()
while True:
    i = input('Choose one: ')

    if i == '1':
        l.adding_books()
    elif i == '2':
        l.adding_client()
    elif i == '3':
        l.listing_books()
    elif i == '4':
        l.listing_clients()
    elif i == '5':
        l.share_book()
    elif i == '6':
        l.delete_book()
    elif i == '7':
        l.listing_shared_books()
    elif i == '8':
        break