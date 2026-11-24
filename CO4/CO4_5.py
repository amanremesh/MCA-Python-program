
class Publisher:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Publisher:", self.name)
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author
    def display(self):
        print("Publisher:", self.name)
        print("Title:", self.title)
        print("Author:", self.author)
class Python(Book):
    def __init__(self, name, title, author, price, no_of_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_of_pages = no_of_pages
    def display(self):
        print("Publisher:", self.name)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("No. of pages:", self.no_of_pages)
b = Python("Tech Publications", "Python Programming",
           "John Smith", 450, 320)
b.display()
