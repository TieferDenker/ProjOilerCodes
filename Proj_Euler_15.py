M = 1000000007

def Solve_Prob(n,m):
    pro = 1
    for i in range(n+1,m+n+1):
        pro = (pro*i)
    answer = pro

    for i in range(1,m+1):
        pro = (pro//i)
    answer = pro

    return answer%M

t = int(input())
for i in range(0,t):
    n,m = map(int,input().split())
    answer = Solve_Prob(n,m)
    print(answer)