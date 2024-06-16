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
    A = 0
    B = 0
    answer = 0
    maxx = -10000000
    for b in range(-n,n+1):
        if prime[abs(b)]:
            for a in range(-n,n+1):
                count = 0
                for n in range(0,abs(b)):
                    x = n**2+a*n+b
                    if (x>1) and prime[x]:
                        count += 1
                if count > maxx:
                    maxx = count
                    A = a
                    B = b
                    # print(A,B,count)
    print(A,B)
    return answer

N = int(10E6)
SieveofE(N)

# t = int(input())
t = 1
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    # print(answer)