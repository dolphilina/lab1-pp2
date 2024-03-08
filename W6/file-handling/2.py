#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os

print('Exist:', os.access('week_6\File_handling', os.F_OK))
print('Readable:', os.access('week_6\File_handling', os.R_OK))
print('Writable:', os.access('week_6\File_handling', os.W_OK))
print('Executable:', os.access('week_6\File_handling', os.X_OK))