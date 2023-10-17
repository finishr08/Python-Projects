
"""
Name: Mustafa Ahmed
Roll no: BSSE-08
Programming Fundamentals

1. How can you use set comprehension to create a new set that contains
the common elements between two given sets?
"""

##set Comprehension

a={1,2,3,4,5,6}
b={2,3,5,8,9,0}
c=a.intersection(b)
d={x for x in c}
print(d)
