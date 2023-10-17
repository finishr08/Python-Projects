##Mustafa Ahmed
##BSSE-08
##Qno6 Assignment no.5(Fibnacci series)

"""
6.Write a Python program that uses the filter function to generate a list
of all Fibonacci numbers that are multiples of 3 between 0 and 100.
"""

def fib(n):
    """Returns the nth Fibonacci number"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Generate the Fibonacci numbers between 0 and 100
fib_numbers = []
i = 0
while fib(i) <= 100:
    fib_numbers.append(fib(i))
    i += 1

# Use filter() to get the Fibonacci numbers that are multiples of 3
fib_multiples = list(filter(lambda x: x % 3 == 0, fib_numbers))

print(fib_multiples)
