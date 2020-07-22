class Animal:
    """Animal class demo"""
    def __init__(self):
        pass

    def say_hi(self):
        print("Hi, I'am an animal.")

    def __repr__(self):
        return "<Object = %s>" % (self.__class__)

animal1 = Animal()
animal1.say_hi()
print(animal1)