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

def IsTrunPri(n):
    global prime
    m = n
    A = []
    k = 10
    for i in range(0,len(str(n))):
        x = n%k
        A.append(x)
        y = n//k
        if not(y == 0):
            A.append(y)
        k = k*10
    count = 0
    for num in A:
        if prime[num]:
            count = count + 1
    if count == len(A):
        return True
    else:
        return False

def Solve_Prob(n):
    summ = 0
    for i in range(10,n):
        if IsTrunPri(i):
            summ = summ + i
    answer = summ
    return answer

SieveofE(1000000)
# t = int(input())
t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)