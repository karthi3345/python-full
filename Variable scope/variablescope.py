#scope= the region that a variable is recognized
#variable is only available from insu=ide the rgion is created
#A global and locally scoped versions of a variable can eb created
name="bro"#global sacope availabel inside &outside of the function
def display_name():
 name = "code" #local scope availabel only inside of the function

print(name)

display_name()
print(name)
