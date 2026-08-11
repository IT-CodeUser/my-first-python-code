# Defining the Class (Blueprint)
class Dog:
    # The Constructor Method
    def __init__(self, name, breed):
        self.name = name    # Instance attribute
        self.breed = breed  # Instance attribute

    # A regular method defining a behavior
    def bark(self):
        return f"{self.name} says Woof!"

# Creating Objects (Instances of the Class)
dog1 = Dog(name="Buddy", breed="Golden Retriever")
dog2 = Dog(name="Max", breed="German Shepherd")

# Accessing attributes and methods using dot notation
print(dog1.name)    # Output: Buddy
print(dog2.bark())  # Output: Max says Woof!




# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

# Child Class inherits from Animal
class Cat(Animal):
    def meow(self):
        return f"{self.name} says Meow!"

# Creating an instance of the child class
my_cat = Cat("Whiskers")
print(my_cat.eat())   # Inherited method output: Whiskers is eating.
print(my_cat.meow())  # Child-specific method output: Whiskers says Meow!
