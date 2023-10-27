class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 5)
print(p.x)
print(p.y)

class Book:
    def __init__(self, title):
        self.title = title

book1 = Book("The Power of Now")
print(book1.title)

class Person():
    def __init__(self, firstname):
        self.firstname = firstname

person1 = Person("Tuyen")
print(person1.firstname)
