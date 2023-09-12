class Addition:
     def add(self):
        a=int(input("enter a value:"))
        b=int(input("enter b value"))
        c=a+b
        print("Addition:",c)

class Subtraction(Addition):
     def sub(self):
        a=int(input("enter a value:"))
        b=int(input("enter b value"))
        c=a-b
        print("Subtraction:",c)   

obj=Subtraction()
obj.add()
obj.sub()
