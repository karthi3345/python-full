#derived child class from parent class
#code reusable

class Version1:
     def v1(self):
       print("button")
       print("textbse")


class Version2(Version1):
    
    def v2(self):
        print("dropdown")

app= Version2()
app.v1()
app.v2()

  