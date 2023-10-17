##Assignment 03 Qno.1
##Programming Fundamentals
##Mustfa Ahmed
##Write a Python program to convert string into date/time object.
##------------------------------------------------------------------------------

import datetime

date_string = "2022-03-11 12:30:00"

date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

print("Date object:", date_object)

##                                End
