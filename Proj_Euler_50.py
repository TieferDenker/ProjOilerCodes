prime = []

def SieveofE(n):
    global prime
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

def Solve_Prob(n):
    summ = 0
    count = 0
    answer = 0
    for i in range(2,n):
        if prime[i]:
            count += 1
            summ = summ + i
            if (summ < n) and prime[summ]:
                p = summ
                l = count
    print(p,l) 
    return answer

t = int(input())
# t = 1
A = []
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    A.append(n)

SieveofE(max(A))
for i in A:
    answer = Solve_Prob(i)
