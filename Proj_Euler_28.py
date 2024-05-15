def Solve_Prob(n):
    if n == 1:
        answer = 1
    else:
        n = (n-1)//2
        summ = (n*(16*n*n+30*n+26))//3
        answer = 1+summ
    return answer%1000000007

t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)