from math import ceil, floor, sqrt

def IsPenta(n):
    m = 2*n
    if (ceil(sqrt(1+12*m)) == floor(sqrt(1+12*m))):
        x = int(sqrt(1+12*m))
        if (x+1)%6 == 0:
            answer = True
        else:
            answer = False
    else:
        answer = False
    return answer

def Solve_Prob(n,k):
    A = []
    for i in range(k+1,n):
        pi = (i*(3*i-1))//2
        pi_minus_k = ((i-k)*(3*(i-k)-1))//2
        if (IsPenta(pi-pi_minus_k) or IsPenta(pi+pi_minus_k)):
            A.append(pi)
    return A   

# t = int(input())
t = 1
for i in range(0,t):
    n,k = map(int, input().split())
    # n = int(input())
    answer = Solve_Prob(n,k)
    # print(answer)
for i in answer:
    print(i)