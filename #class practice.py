#class practice

class Car:
    
    wheels = 4

    def __init__(self, make, model, year, color):
        self.make = make # instance variable
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")

car_1 = Car("Chevy", "Corvette",2021, "blue")
print(car_1.make)
car_1.drive()
car_1.stop()
car_1.wheels = 2v


class Organism:
    alive = True


class Animal(Organism):
    def eat(self):
        print("This animal is eating")



class Animal:
    
    alive = True

    def eat(self):
        print("This animal is eating")
        return self
    
    def sleep(self):
        print("This animal is sleeping")
        return self

class Rabbit(Animal):
    pass

class Fish(Animal):
    pass

class Hawk(Animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

fish.eat()\
    .sleep()

hawk.sleep()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height


#Abstract class: a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")


vehicle = Vehicle()


class Car:
    color = None


def change_color(car, color):

    car.color = color
car_1 = Car()

change_color(car_1, "red")

#duck typing: of it walks like a duck, quacks like a duck, then it must be a duck