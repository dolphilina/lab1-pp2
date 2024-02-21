'''
Write a Python program to calculate two date difference in seconds.
'''

from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.strptime(input("Enter first date and time in format 'Year-Month-Day Hours:Minutes:Seconds': "), '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(input("Enter second date and time in format 'Year-Month-Day Hours:Minutes:Seconds': "), '%Y-%m-%d %H:%M:%S')
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))