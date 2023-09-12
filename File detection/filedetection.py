import os

path="C:\\Users\\lkart\\Desktop\\Python full\\File detection\\file folder"
if os.path.exists(path):
  print("The Location exists") 
if os.path.isfile(path):
  print("That is a file")
elif os.path.isdir(path):
  print("that is directory")
else:
  print("The Location doesn't exists")

