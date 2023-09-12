#Random numbers 
import random
x= random.randint(1,6)
y=random.random()
mylist=["rock","paper","Scisors"]
z=random.choice(mylist)
print(z)
cards=[1,2,3,4,5,6,7,8,9,"j","Q","k","A"]
random.shuffle(cards)
print(cards)