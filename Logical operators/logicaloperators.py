#logical operators(AND OR not )
#used to check if two or more conditional statement true
temp=int(input("what is your temperature outside:"))
if not(temp>=0 and temp<=30):
    print("temperaturte is good today")
    print("go outside:")
elif not(temp<=0 or temp>32):
    print("temp is bad")   
    print("sit inside")
#not makes true to false or false to true