"""
Name: Mustafa Ahmed
Roll No: Bsse-08
Course: Programming Fundamentals

20.Random Password Generator: Write a Python program that generates a random password using
a combination of letters, digits, and symbols. The program can let the user specify the
length and complexity of the password.

"""
print()
print("----------------------------------------")
print("|Welcome to 'Random Password Generator'| ")
print("----------------------------------------")

import random

while True:
    complexity = input("Enter the complexity level (low/medium/high): ")
    if complexity == 'low':
        characters = "abcdefghijklmnopqrstuvwxyz0123456789&*()_"
    elif complexity == 'medium':
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^"
    else:
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:<>,.?/~"

    length = int(input("Enter the length of required password: "))
    count = int(input("Enter the number of required passwords: "))

    for i in range(count):
        password = ""
        for j in range(length):
            character = random.choice(characters)
            password = password+character
        print("The random generated password is:", password)

    again = input("Do you want to generate more passwords.....? (y/n) ")
    if again == "n":
        break
print()
print("----------------------------------")
print("|Thanks for generating passwords!|")
print("----------------------------------")


    
