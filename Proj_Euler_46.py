import random
from math import sqrt

# Small primes for deterministic primality testing
SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def is_prime(n, k=5):
    if n in SMALL_PRIMES:
        return True
    if n <= 1 or n % 2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0 or n%11 == 0 or n%13 == 0 or n%17 == 0 or n%19 == 0 or n%23 == 0 or n%29 == 0 or n%31 == 0 or n%37 == 0 or n%41 == 0 or n%43 == 0 or n%47 == 0:
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
    x = int(sqrt(n/2))
    count = 0
    for i in range(1,x+1):
        if is_prime(n-2*i*i):
            count = count + 1
    answer = count
    return answer

t = int(input())
# t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)