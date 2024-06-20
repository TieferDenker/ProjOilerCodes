def pfac(n):
    dispfac = 0
    if n%2 == 0:
        dispfac += 1
        while n%2 == 0:
            n = n//2

    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            dispfac += 1
            while n%i == 0:
                n = n//i
    if n>2:
        dispfac += 1

    return dispfac

def Solve_Prob(n,k):
    answer = 0
    for i in range(14,n+1):
        count = 0
        for j in range(0,k):
            if (pfac(i+j) == k):
                count += 1
        if count == k:
            print(i)
    return answer

# t = int(input())
t = 1
for i in range(0,t):
    n,k = map(int, input().split())
    # n = int(input())
    answer = Solve_Prob(n,k)
    # print(answer)