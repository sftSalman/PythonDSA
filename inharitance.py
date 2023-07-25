from abc import ABC,abstractmethod
class Book(ABC):
    def __init__(self,title,quantity,author,price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.__size = None

    def set_size(self,size):
        self.__size = size
    def isFree(self):
        if self.__size =='big':
            return print('the book is free')
    @abstractmethod
    def print(self) :
        return print ( f"the name is {self.title} and price is {self.price} " )





class Novel(Book):
    def __init__(self,title,quantity,author,price,pages):
        super().__init__(title,quantity,author,price)
        self.pages = pages
    def print(self) :
        return print ( f"the name is {self.title} and price is {self.price} and pages is {self.pages} " )


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch) :
        super().__init__()
        self.branch = branch




b1 = Novel('sea',1,'salman',100,10)
b1.print()

b1.set_size('big')
b1.isFree()