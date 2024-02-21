'''
Write a Python program to drop microseconds from datetime.
'''

import datetime
dt = datetime.datetime.today().replace(microsecond=0)
print(dt)
