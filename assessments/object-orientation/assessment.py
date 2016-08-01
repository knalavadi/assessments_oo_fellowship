"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

	   encapsulation: keeps related things together 

	   abstraction: you dont need to know the information a method uses. 

	   polymorphism: interchange the compoents  

2. What is a class?
	class is a type. it holds shared attributes which are applicable to all members of that class

3. What is an instance attribute?
	is given when that instance is intiated 

	def __init__(self, name):
		self.name = name 

4. What is a method?
	a function defined on a class 
		def name(self):
			return "Krisha"

5. What is an instance in object orientation?
	is an indivdual instance of that class, a class

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   a class attribute is an attribute that all instances of that class
    (and decendents of that class) will have.  SO if you want all decendents 
    of that class to hav that attribute 

    	eg. 
    	def __init__(self, name, color, moves, num_wheels):
		self.moves = True
   
   an instance attribute is an attribute that only affects that instance of the class. this will override 
   
   eg. in the example below - if you had a yellow bike (not all bikes are yellow)


"""


# Parts 2 through 5:
# Create your classes and class methods

class AbstractTransportation(object): #Abstract class taking in the methods, 
#name, color, moves and number of wheels 

	def __init__(self, name, color, moves, num_wheels):
		self.name = name
		self.color = color 
		self.moves = True
		self.num_wheels = num_wheels



class Bike(AbstractTransportation):

	def __init__(self):
		return super(Bike, self).__init__("bike", color, 2)

class Car(AbstractTransportation)	

	def __init__(self, has_airbags):  # a new method has_airbags which is unique to cars
		return super(Car, self).__init__("car", color, 4)

		self.has_airbags = True









