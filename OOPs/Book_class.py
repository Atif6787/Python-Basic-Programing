class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_title(self):
        print(f"This book name is {self.title}.")

    def display_author(self):
        print(f"It is written by {self.author}.")

    def display_price(self):
        print(f"And its price is {self.price}.")


book1 = Book("Python Basics", "John Doe", 500)
book1.display_title()
book1.display_author()
book1.display_price()

