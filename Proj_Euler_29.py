from math import log, gcd

def f(n):
    count = 0
    while n%2 == 0:
        n = n//2
        count += 1

    g = count
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            count = 0
            while n%i == 0:
                n = n//i
                count += 1
            g = gcd(g,count)
    if n>2:
        return False

    if g > 1: 
        return True
    else:
        return False

def Solve_Prob(n):
    count = (n-1)*(n-1)
    for i in range(2,n+1):
        if not(f(i)):
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

# t = int(input())
t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)

