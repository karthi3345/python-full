# 2basesses accesss by one derived class
class Add:
    def  add(self):
      a=int(input("enter a value:"))
      b=int(input("enter b value"))
      c=a+b
      print("addition", c)

class Sub:
   def sub(self):
     a=int(input("enter a value:"))
     b=int(input("enter b value"))
     c=a-b
     print("subtraction",c)

class Input (Add,Sub):
    def base(self):
        self.add()
        self.sub()

obj=Input()
obj.base()

