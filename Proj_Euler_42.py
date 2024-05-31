from math import ceil, floor, sqrt

def Solve_Prob(n):
    m = 2*n
    if (ceil(sqrt(1+4*m)) == floor(sqrt(1+4*m))):
        x = int(sqrt(1+4*m))
        if (x-1)%2 == 0:
            answer = (x-1)//2
        else:
            answer = -1
    else:
        answer = -1
    return answer

t = int(input())
# t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)