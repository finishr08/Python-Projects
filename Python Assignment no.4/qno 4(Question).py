"""
Name: Mustafa Ahmed
Roll no: BSSE-08
Programming Fundamentals

4. How can you use Counter to count the occurrences of
each character in a given string, ignoring spaces and punctuation?
"""

from collections import Counter
import string

def count_chars(s):
    # Remove spaces and punctuation from the string
    s = s.translate(str.maketrans("", "", string.punctuation + " "))
    # Use Counter to count the occurrences of each character
    return Counter(s)

# Example usage:
s = "Hello, World!"
print(count_chars(s))
