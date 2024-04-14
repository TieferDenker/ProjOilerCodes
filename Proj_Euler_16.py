def Solve_Prob(n):
    m = int(2**n)
    s = str(m)
    i = 0
    summ = 0
    while i < len(s):
        summ = summ + int(s[i])
        i = i + 1
    answer = summ
    return answer

t = int(input())
for i in range(0,t):
    # n,m = map(int,input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)