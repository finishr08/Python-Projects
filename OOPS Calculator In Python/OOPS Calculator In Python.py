"""
Name: Mustafa Ahmed
Roll no: PUT-BSSE-08
Course: Object Oriented Programming
"""
print("""
===========================================
| Calculator Program Using OOPS in Python |
===========================================""")

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

calculator = Calculator()

while True:
    print()
    print\
("""Select operation
1. Add")
2. Subtract")
3. Multiply")
4. Divide")
5. Quit""")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("""
================================
| Calculator program has ended |
================================""")
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", calculator.add(num1, num2))
        elif choice == '2':
            print("Result:", calculator.subtract(num1, num2))
        elif choice == '3':
            print("Result:", calculator.multiply(num1, num2))
        elif choice == '4':
            print("Result:", calculator.divide(num1, num2))
    else:
        print("Invalid choice. Please select a valid operation.")

    restart = input("Do you want to start again? Press 'y': ")
    if restart.lower() != 'y':
        print("""
        ================================
        | Calculator program has ended |
        ================================""")
        break
