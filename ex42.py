# Animal is-a object
class Animal(object):
	pass

# Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		# Dog has-a name
		self.name = name

# Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		# Cat has-a name 
		self.name = name

# Person is-a object
class Person(object):

	def __init__(self, name):
		# Person has-a name
		self.name = name

		# Person has-a pet of some kind
		self.pet = None

# Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		# Employee has-a salary
		self.salary = salary

class Fish(object):
	pass

class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

# rover is-a Dog named Rover (and an Animal)
rover = Dog("Rover")

# satan is-a Cat named Satan (and an Animal)
satan = Cat("Satan")

# mary is-a Person named Mary
mary = Person("Mary")

# Frank is-a Employee named Frank with salary 120000 (and a Person)
frank = Employee("Frank", 120000)

# frank has-a pet which is rover
frank.pet = rover

# flipper is a Fish
flipper = Fish()

# crouse is-a Salmon (and a Fish)
crouse = Salmon()

# harry is-a Halibut (and a Fish)
harry = Halibut() 
