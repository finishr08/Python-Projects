##Assignment 03 Qno.2
##Programming Fundamentals
##Mustfa Ahmed

##Write a Python program to check whether two lists have
##at least one element in common.
##------------------------------------------------------------------------------

list1 = input("Enter element for list1: ")
list2 = input("Enter element for list2: ")
if set(list1).intersection(list2):
    print("The two lists have at least one element in common.",set(list1).intersection (list2))
else:
    print("The two lists do not have any elements in common.")



##                               End
