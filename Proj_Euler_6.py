def Solve_Prob(n):
    s1 = (n*(n+1)*(2*n+1))//6
    s2 = (n*(n+1))//2
    answer = abs(s1-s2**2)
    return answer

t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)