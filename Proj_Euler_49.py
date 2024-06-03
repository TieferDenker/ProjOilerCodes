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

def toString(List): 
    return ''.join(List) 

Permuations = []
def permute(a, l, r):
    global Permuations
    if l == r:
        Permuations.append(int(toString(a)))
    else: 
        for i in range(l, r): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]
    return Permuations 

def IsPrimeAP(n,k):
    global Permuations
    flag = False
    Permuations = []
    ansdiff = []

    string = str(n)
    l = len(string) 
    a = list(string) 
    Per = permute(a, 0, l)
    tempset = set(Per)
    UniqPer = list(tempset)
    # print(UniqPer)

    PrimeUniqPer = []
    for i in UniqPer:
        if is_prime(i):
            PrimeUniqPer.append(i)
    # print(PrimeUniqPer)

    if k == 3:
        for i in range(0,len(PrimeUniqPer)):
            x = PrimeUniqPer[i]-n
            if (x>0) and ((n+2*x) in PrimeUniqPer):
                flag = True
                ansdiff.append(x)
    else:
        for i in range(0,len(PrimeUniqPer)):
            x = PrimeUniqPer[i]-n
            if (x>0) and ((n+2*x) in PrimeUniqPer) and ((n+3*x) in PrimeUniqPer):
                flag = True
                ansdiff.append(x)

    # print(n,flag,ansdiff)
    return flag,ansdiff

# N = 1000000
def Solve_Prob(n,k):
    A = []
    D = []
    answer = ""

    for i in range(1000,n):
        if is_prime(i):
            flag,diff = IsPrimeAP(i,k)
            if flag:
                for j in range(0,len(diff)):
                    A.append(i)
                    D.append(diff[j])
    # print(A)
    # print(D)

    for i in range(0,len(A)):
        answer = ""
        a = A[i]
        d = D[i]
        for j in range(0,k):
            x = str(a+j*d)
            answer = answer + x
        print(answer)  
    return answer

# t = int(input())
t = 1
for i in range(0,t):
    n,k = map(int, input().split())
    # n = int(input())
    answer = Solve_Prob(n,k)
    # print(answer)