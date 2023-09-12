#Recrursion= Function which call itself is called recursion
#helps to visualize complex problem in basic steps
#WHICH CAN BE SOLVED more iteratively or recrusively

#Iteravtive
#def walk(steps):


 #for step in range(1, steps+1):
    #print(f"youn take step#{step}")
    
def walk(steps):
    print(f"you take step#{steps}")
    walk(steps-1)



walk(100)