"""
Name: Mustafa Ahmed
Roll no: BSSE-08
Programming Fundamentals

6. How can you use defaultdict to group a list of words
by their first letter?
"""

from collections import defaultdict

# Define a list of words
words = ['apple', 'banana', 'cherry', 'date']

# Create a defaultdict with list as default_factory
word_dict = defaultdict(list)

# Group the words by their first letter
for word in words:
    word_dict[word[0]].append(word)

# Print the resulting dictionary
print(word_dict)
