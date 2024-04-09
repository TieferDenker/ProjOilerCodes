import math
import random

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

def Solve_Prob(n):
    power2 = math.floor(math.log2(n))
    lcm = 2**power2
    for i in range(3,n+1,2):
        if is_prime(i):
            power = math.floor(math.log(n,i))
            lcm = lcm * (i**power)
    return lcm

t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)