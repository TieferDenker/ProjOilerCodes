def Solve_Prob(n):
    answer = -1
    for a in range(1,n):
        for b in range(1,n):
            answer = max(sum(map(int,list(str(a**b)))),answer)
    return answer

t = 1
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)