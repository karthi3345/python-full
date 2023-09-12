#parameter that  apack all arugument in to dictiory 
#so the function can accept the value amount of keyword argument
#keyword **kwargs
def hello(**kwargs):
   # print ("Hello"+kwargs+ ["first"] +" " +kwargs["last"])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")


hello(title="Mr",first="Bro",middle="Dude",last="code")

   