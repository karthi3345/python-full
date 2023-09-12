# copy file()= copy the content of a file
#copy()= copyfile()+ permission mode+ destination can be a directory
# copy2()= copy()+ copies metadata (file' creation and modification times)

import shutil
shutil.copy2("C:\\Users\\lkart\\Desktop\\Python full\\Read file\\text.txt",'C:\\Users\\lkart\\Desktop\\Python full\\copy file\\copy.txt')