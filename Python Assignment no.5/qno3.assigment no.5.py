##Mustafa Ahmed
##BSSE-08
##Qno3 Assignment no.5(Fibnacci series)

"""3.	Write a Python program that uses the reduce function
to calculate the sum of the first 20 Fibonacci numbers.
"""

from functools import reduce

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib_numbers = map(fib, range(20))


fib_sum = reduce(lambda x, y: x + y, fib_numbers)

print(fib_sum)
