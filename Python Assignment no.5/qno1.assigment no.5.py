##Mustafa Ahmed
##BSSE-08
##Qno1 Assignment no.5(Fibnacci series)

"""1.	Write a Python program to generate
a sequence of Fibonacci primes (prime numbers in the Fibonacci sequence)? 
"""

def is_prime(n):
    if n <= 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def fibonacci_primes(n):
    a, b = 1, 1
    while n > 0:
        if is_prime(a):
            yield a
            n -= 1
        a, b = b, a + b

n = int(input("Enter the number of Fibonacci primes you want to generate: "))
for num in fibonacci_primes(n):
    print(num)
