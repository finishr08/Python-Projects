"""
Name: Mustafa Ahmed
Roll no: BSSE-08
Programming Fundamentals

5. How can you use ChainMap to combine two dictionaries
and access the merged result as a single dictionary?
"""
from collections import ChainMap

# Create two dictionaries to merge
dict1 = {1: 11, 2: 22}
dict2 = {3: 33, 4: 44}

# Create a ChainMap object with the two dictionaries
merged_dict = ChainMap(dict1, dict2)

# Access the merged result as a single dictionary
print(merged_dict[1])  
print(merged_dict[2])  
print(merged_dict[3])  
print(merged_dict[4])  
