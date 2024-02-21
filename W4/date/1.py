'''
Write a Python program to subtract five days from current date.
'''

from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('today is',date.today())
print('5 days ago was',dt)