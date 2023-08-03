# https://www.freecodecamp.org/news/object-oriented-programming-in-python/
from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.price * (1 - self.__discount)
        return self.price

    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

    def get_price(self):
        if self.pages > 150:
            return super().get_price() * 0.8  # Applying additional 20% discount for novels with more than 150 pages

    def __repr__(self):
        return f"Price: {self.get_price()}"


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def get_price(self):
        if self.author=='salman':
            return super().get_price()*.0


    def __repr__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)
print(novel1)

academic1 = Academic('Python Foundations', 12, 'salman', 655, 'IT')
print(academic1)
