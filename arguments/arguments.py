#args= paramater that will pack all arguments in to the tuple usee
#useful so that a function can accept a avrying the  amount of argument
def add(*stuff):
    sum=0
    stuff=list(stuff)
    stuff[0]=0
    for i in stuff:
        sum+=i
    return sum


print(sum(1,2,3,4,5,6))