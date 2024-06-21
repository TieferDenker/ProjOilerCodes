import random

# Small primes for deterministic primality testing
SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def isprime(n, k=5):
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
    
def isprime1(n):
    if n in SMALL_PRIMES:
        return True
    for i in SMALL_PRIMES:
        if n%i == 0:
            return False

    while n%2 == 0:
        return False
        n = n//2

    for i in range(3,int(n**0.5)+1,2):
        while n%i == 0:
            return False
            n = n//i
    if n>2:
        return True

def Solve_Prob(n):
    k = 1
    count = 0
    while True:
        s = (2*k+1)**2
        a = s-6*k
        b = s-4*k
        c = s-2*k
        if isprime(a):
            count += 1
        if isprime(b):
            count += 1
        if isprime(c):
            count += 1
        dia = 4*k+1
        percent = int((count/dia)*100)
        if percent < n:
            return 2*k+1
        k += 1

# t = int(input())
t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)