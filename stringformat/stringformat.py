# str.format()= optional method that give  users more control when 
#displaying output
animal="cow"
item="moon"
#print("The "+animal+ "jumped over the" " " + item)
#print("The {} jumped over the {}".format(item,animal))
#print("The {1} jumped over the {0}".format(item,animal))#positional argument
#print("The {item} jumped over the {animal}".format(item="cow", animal="moon"))#keyword argument
text="the{} jumped over the {}"
print(text.format(animal,item))