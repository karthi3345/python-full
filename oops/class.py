class Oops:#class is a template or blue print  or memoryspace
   #object is state and behavior
   #behavior= methid/function

 def func1(self, name ,age): #method
    self.name=name
    self.age =age

    print("name:" ,self.name)

 def func2(self, rollno):
    self.rollno=rollno
   
    print("my age ", self.age, )
    print("my  roll no ", self.rollno )


obj= Oops() #CLASS MEMPRY ACCES PANDREN ATHULA OBJECT okkara vachuruken
#obj= object name
#oops= ref name
#object represents ofg class 
#object is the instance of class
obj.func1("karthik","25")
obj.func2("22")