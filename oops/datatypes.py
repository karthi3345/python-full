#data types in python
#this is dynamic type programming lanuguage
#this information tells about what thype data

#int , string first edhytovidiane jkuduka thevailla
#duck type programming language
#explicity we never mention variables/identifiers

#based on value python will automatically assign corresponding datadtypes
#int
#float
#bool
#str
#range
#byte array
#range
#list
#frozen set
#tuple
#dict
#none total 14 data types

no=10
print(type(no) )#parameter/#argument

no1=0.5
print(type(no1))
result=True
print(type(result))

aks="tjs"
print(type(aks))

Market=["apple","orange","papaya"]
print(type(Market))

#type= what data type
#id=#address

#num_1=15
####num2=446.97748748


no=bin(20)
print(no)
no=oct(20)
print(no)

no=hex(20)
print(no)

no2=7.7e3
print(no2)

no=7.7E3
print(no)
#____complex Datatype_______#

#real Part +imaginary part#

no1=5+10j
print(type(no1))

no2=10+3j

total=no1+no2
print('Total is',+total)

print(no2.real)
print(no2.imag)

#_____bool_____#
no1=10 #equal is assignment operator
no2=15
print(no1>no2)
print(no1<no2)
print(no1==no2) #33threasu mari
print(no1!=no2)
present=True
print(present)

print(True+True)
print(False+False)
print(True+False)

#str is primitive datatype

name='karthik'
print(name)

print(len(name))
sen=""" muthus's mail is lkatysjhj@gmail.com and he said  "Hi" """
print(sen)

address=""""
7171 karpaganagar 6th street
k.pudur
madurai-625007



"""
print(address)
name="karthik"
pin=625007
print(name,pin)

#--------string slicing_______#
name= "Karthik Raja"
print("" ,name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
print(name[9])
print(name[10])
print(name[11])

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
#forward +ve start from 0
#backward -ve start from-1

#-------------------------------------#

king="Rajarajacholan"
print(king[0:5])
print(king[7:])
print(king[:4])
print(king[4:])
print(king[0:5:2])
a="abcdefghijklmnopqrstuvwxyz"
print(a[0:5])
print(a[-1:])
print(a[5:10])
print(a[5:-1])
print(a[-5:-1])
print(a[-5:-2])
print(a[::])
print(a[1:5])
print(a[1:10])
print(a[1:10:2])
print(a[2:16:3])
print(a[8:1:-1])
print(a[8:1:-2])
print(a[1:8])
print(a[1:8:3])
print(a[10:1:-2])
print(a[11:1:-2])
print(a[-26:-1])
print(a[-26:-1:2])
print(a[-26:-1:5])
n="karthik"
val=len(n)

print(n[-val:val])
print(n[(val-1):0:-1])
print(n[::])
print(n[::-1])
print(n[5:-4])
print(n[::4])


k='muthuramalingam'

print(k[::-1])
print(k[5:-5])
print(k[10:1:-2])
print(k[2:6])
print(k[6:1:-1])
print(k[1:6])
print(k[1:-1])
print(k[0:-2])
print(k[6:2:-4])
print(k[10:1:-2])
print(k[10:1:-1])
print(k[::4])
print(k[1::-1])
print(k[1::8])
print(k[::1])

name='True'
print(name*3)