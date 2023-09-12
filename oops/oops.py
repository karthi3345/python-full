#object is  instance of class using programming we can create real life object
class Car:
 

 def __init__(self, make ,model, year, color):
    self.model=model
    self.make= make
    self.year=year
    self.color=color

 def drive(self):
    print("This car is driving ")


 def stop(self):
    print("this car is start ")
