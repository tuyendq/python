## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

# is-a
class Dog(Animal):

	def __init__(self, name):
		# has-a
		self.name = name

# is-a
class Cat(Animal):

	def __init__(self, name):
		# has-a
		self.name = name

# is-a
class Person(object):

	def __init__(self, name):
		# has-a
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## is-a
class Employee(Person):

	def __init__(self, name, salary):
		## has-a hmm what is this strange magic?
		super(Employee, self).__init__(name)
		# has-a
		self.salary = salary

## is-a
class Fish(object):
	pass

## is-a
class Salmon(Fish):
	pass

## is-a
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is an Employee, has-a salary
frank = Employee("Frank", 120000)

## frank has-a pet
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
