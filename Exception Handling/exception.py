#exception = events detected executio that interrupt rhe flow of program

try:
  numerator = int(input("Enter number to divide:"))
  denominator=int(input("enter a number to divide by:"))
  result= numerator/denominator
  print(result)
except ZeroDivisionError as e:
   
   print("you can't divide by zero idiot")
   print(e)
except ValueError as e:
  print("enter only number please")
  print(e)
except Exception as e:
   #print("something went wrong:")
   print(e)
else:
  print(result)
finally:
  print("this will always execute")