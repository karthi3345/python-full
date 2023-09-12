#ifstatement is block of code it exexcute only if condiution true
age=int(input("how old are you:"))
if age==100:
    print("you are centuryold:")
elif age>=18:
    print("you are adult:")

elif age<0:
     print("you not born:")
else:
    print("you are child")
