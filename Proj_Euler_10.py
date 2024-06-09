PRIMES = []
SUM = []

def SieveOfEratosthenes(n):
    global PRIMES
    PRIMES = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (PRIMES[p] == True):
            for i in range(p * p, n+1, p):
                PRIMES[i] = False
        p += 1
    PRIMES[0],PRIMES[1] = False,False

def SumPrime(n):
    global SUM
    summ = 0
    for i in range(0,n+1):
        if PRIMES[i]:
            summ = summ + i
        SUM.append(summ)        

def Solve_Prob(n):
    global SUM
    answer = SUM[n]
    return answer

SieveOfEratosthenes(int(10E5))
SumPrime(int(10E5))
# print(SUM)

t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)
