from math import log

prime = []

def f(n):
    pfac = 0
    if (n%4 == 0) or (n%9 == 0) or (n%25 == 0) or (n%49 == 0) or (n%121 == 0):
        return False,-1

    if n%2 == 0:
        pfac += 1
        n = n//2

    for i in range(3,int(n**0.5)+1,2):
        if prime[i] and (n%i == 0):
            pfac += 1
            count = 0
            while n%i == 0:
                n = n//i
                count += 1
            if count > 1:
                return False,-1
    if n>2:
        pfac += 1
    if pfac%2 == 0:
        return True,-1
    else:
        return True,1

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
    count = (n-1)*(n-1)
    for i in range(2,n+1):
        if prime[i]:
            l = int(log(n,i))-1
            k = 2
            summ = 0
            while (l>0):
                summ = summ + int(n/k) - 1
                k += 1
                l -= 1
            count -= summ
    answer = count
    return answer

N = int(10E4)
SieveofE(N)
# print(N**N)

# t = int(input())
t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)