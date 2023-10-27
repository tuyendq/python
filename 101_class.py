class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 5)
print(p.x)
print(p.y)

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_price(self):
        return self.price

book1 = Book("The Power of Now", "Eckhart Tolle", 9.99)
print(book1.title)
print(book1.author)
print(book1.get_price())

print(type(book1))
print(isinstance(book1, Book))  # Should be True
print(isinstance(book1, Point))  # Should be False

class Person():
    def __init__(self, firstname):
        self.firstname = firstname
        # Just a convention for hidden attribute, but you can hack it
        self.__secret = "This is a secret attribute! But you can hack it."

    """One way to create a static method"""
    @staticmethod
    def get_person():
        print(">>> What is static method used for?")


# Go ahead, just call static method without creating an instance
print(Person.get_person())

person1 = Person("Tuyen")
print(person1.firstname)



print(person1._Person__secret)  # You can hack hidden attribute
print(person1.__secret)  # Should get AttributeError error (no __secret attr)

