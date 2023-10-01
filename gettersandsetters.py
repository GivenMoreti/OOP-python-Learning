# classes
class Book:
    #    attribute
    def __init__(self, author, title, quantity, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__discount = None
        self.__price = price
# method 1/setters
# using getters and setter to hide some attributes/ or set self.__discount to private

    def set_discount(self, discount):
        self.__discount = discount
# method 2/ getters
# using getters and setter to hide some attributes/ or set self.__discount to private

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price

# string representation to avoid printing out only memory location
    def __repr__(self):
        return f"Book:{self.title} price :{self.get_price()}"


# inheritance
class Novel(Book):
    def __init__(self, author, title, quantity, price, pages):
        super().__init__(author, title, quantity, price)
        self.pages = pages


# using getters and setter to hide some attributes/ or set self.__discount to private
single_book = Book("oke", "any", 1, 300)
bulk_books = Book("oke", "try", 3, 300)
bulk_books.set_discount(0.20)
# after inheritance with added parameter of pages
novel1 = Novel("james", "finance", 2, 450, 600)
novel1.set_discount(0.33)
print(novel1.get_price(),)


# print(single_book.get_price())
# print(bulk_books.get_price())
