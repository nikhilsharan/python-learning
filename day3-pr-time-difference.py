#  Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
import datetime

date1 = input("Enter the latest date in YYYY:MM:DD format:").split(':')
date2 = input("Enter the older date in YYYY:MM:DD format:").split(':')
date11 = datetime.date(int(date1[0]), int(date1[1]), int(date1[2]))
date22 = datetime.date(int(date2[0]), int(date2[1]), int(date2[2]))
# difference = 0
#
#
# difference_year = int(date1[0]) - int(date2[0])
# if difference_year == 0:
#     if date1[1] > date2[1]:
#         difference_month = int(date1[1])-int(date2[1])
#     elif date1[1] == date2[1]:
#         difference_month = 0


print(date11 - date22)
