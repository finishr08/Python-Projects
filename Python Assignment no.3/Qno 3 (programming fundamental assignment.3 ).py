##Assignment 03 Qno.3
##Programming Fundamentals
##Mustfa Ahmed

##Write a Python program to add 3 days and 10 hours to any given date.
##------------------------------------------------------------------------------
import datetime

initial_date_input = input("Enter a date (format: yyyy-mm-dd): ")

initial_date = datetime.datetime.strptime(initial_date_input, "%Y-%m-%d")

new_date = initial_date + datetime.timedelta(days=3, hours=10)

print("The new date is:", new_date.strftime("%Y-%m-%d %H:%M:%S"))




##                               End
