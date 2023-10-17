##Mustafa Ahmed
##BSSE-08
##Qno5 Assignment no.5(Fibnacci series)

"""5.How do you generate the Fibonacci
sequence in reverse order using Python?
"""

def fib(n):
    """Returns the first n Fibonacci numbers"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

n = int(input("Enter Range: "))
fib_sequence = fib(n)
fib_sequence.reverse()

print(fib_sequence)
