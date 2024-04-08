from math import log, floor, sqrt
import random

phi = 1.6180339887498948482045868343656381177203091798057628621354486227052604628189
sq5 = 2.2360679774997896964091736687312762354406183596115257242708972454

# Small primes for deterministic primality testing
SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def is_prime(n, k=40):
    if n in SMALL_PRIMES:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Write n as d*2^r + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def Max_Pri(n):
    sprime = 1
    m = n
    for i in range (3,int(sqrt(n))+1,2):
        while(n%i == 0):
            n = n/i
            sprime = i
    bprime = int(m//sprime)
    return bprime

def Solve_Prob(n):
    if is_prime(n):
        bprime = n
    else:
        if n%2 == 0:
            expo = 0
            while(n%2 == 0):
                n = n/2
                expo = expo + 1
            # print(expo)
            if (n == 1):
                bprime = 2
            else:
                bprime = Max_Pri(n)
        else:
            bprime = Max_Pri(n)
    return bprime


t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)