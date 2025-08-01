#Single inheritance
#Problem 1

class Vehicle:
    def start(self):
        print("Starting the vehicle")
    
class Bike(Vehicle):
    def pedal(self):
        print("Pedaling the bike")

#Problem 2
class Animal:
    def make_sound(self):
        print("Some generaic sound")
class Dog(Animal):
    def fetch(self):
        print("Dog Fetching the ball")

#Multilevel Inheritance
#Problem 1
class Person:
    def introduce(self):
        print(f"Hi, I am a person")

class Employee(Person):
    def work(self):
        print("I am working")

class Manager(Employee):
    def manage(self):
        print("I am manageing the team")


#Problem 2
class Device:
    def power_on(self):
        print("Device powered on")

class Phone(Device):
    def make_call(self):
        print("Calling...")

class Smartphone(Phone):
    def browse_internet(self):
        print("Browsing internet")

#Hierarchical Inheritance
#Problem 1
class Shape:
    def description(self):
        print("This is a shape")

class Rectangle(Shape):
    def description(self):
        print("This is a rectangle")

class Circle(Shape):
    def description(self):
        print("This is a circle")

#Problem 2
class Appliance:
    def plug_in(self):
        print("Appliance plugged in")

class WashingMachine(Appliance):
    def wash_clothes(self):
        print("washing clothes")

class Refrigerator(Appliance):
    def cool_items(self):
        print("Cooling items")


#Multiple Inheritance
#Problem 1

class Flyer:
    def fly(self):
        print("Flying high")

class Swimmer:
    def swim(self):
        print("Swimming fast")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")


#Problem 2
class Writer:
    def write(self):
        print("Writing a book")

class Speaker:
    def speak(self):
        print("Speaking at event")

class Author(Writer, Speaker):
    def introduce(self):
        print("I am an author")