class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def __init__(self, radius):

        super().__init__()
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
    


class Animal:
    def make_sound(self):
        print("Animal sound")


class Cow(Animal):

    def make_sound(self):
        print("Moo")

class Snake(Animal):
    def make_sound(self):
        print("Hiss")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display(self):
        super().display()
        print(f"My grade is {self.grade}.")