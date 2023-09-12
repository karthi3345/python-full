import os
source="C:\\Users\\lkart\\Desktop\\Python full\\movefile\\movefolder"
destination="C:\\Users\\lkart\\Desktop\\movefolder"
try:

  if os.path.exists(destination):
    print("thereis already a file there")
  else:
        os.replace(source,destination)
        print(source+"was moved")

except FileNotFoundError:

     print(source+ "was not found")