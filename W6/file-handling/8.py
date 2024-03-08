#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os

if os.path.exists("deleted.txt"):
  os.remove("deleted.txt")
else:
  print("The file does not exist")