##Mustafa Ahmed
##BSSE-08
##Qno4 Assignment no.5(Fibnacci series)

"""4.Is it possible to generate the Fibonacci sequence in
Python using a generator function? If so, how would you implement it?
"""

def fib():
##    A generator function that generates the Fibonacci sequence
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
n = int(input("Enter Range: "))
fib = fib()

for i in range(n):
    print(next(fib))
print(type(fib))
