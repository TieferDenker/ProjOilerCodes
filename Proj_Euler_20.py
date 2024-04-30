def Solve_Prob(n):
    pro = 1
    for i in range(1,n+1):
        pro = pro * i
    dig = len(str(pro))
    summ = 0
    for i in range(1,dig+1):
        summ = summ + pro%10
        pro = pro//10
    answer = summ
    return answer

t = int(input())
for i in range(0,t):
    # n,m = map(int,input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)