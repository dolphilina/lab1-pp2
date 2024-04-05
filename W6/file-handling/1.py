#Write a Python program to list only directories, files and all directories, files in a specified path.

import os
 
path = "W6\\file-handling"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
print(dir_list)
