##Mustafa Ahmed
##BSSE-08
##Qno2 Assignment no.5(Fibnacci series)

"""2.	Write a Python program that uses the map
function to generate a list of the first 10 Fibonacci numbers.
"""
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci_numbers = list(map(fibonacci, range(10)))

print(fibonacci_numbers)
