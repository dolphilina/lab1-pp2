'''
Write a Python program to print yesterday, today, tomorrow.
'''

from datetime import date, timedelta
dt = date.today() + timedelta(1)
dy = date.today() - timedelta(1)
print('yesterday was',dy)
print('today is',date.today())
print('tomorrow will be',dt)