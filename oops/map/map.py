#has two paramaters function ,iteratable map takes function to argument and applies all function in iterable 


def square(n):
    return(n*n)

listnum=[2,3,4,5]

result=map(square,listnum)

print(list(result))