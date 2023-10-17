"""
Name: Mustafa Ahmed
Roll no: BSSE-08
Programming Fundamentals

3. Can you use list comprehension to create a new list with
elements that are the squares of the odd numbers from 1 to 10?
"""
##List Comprehension

a=[x**2 for x in range(10)if x%2!=0]
print(a)

