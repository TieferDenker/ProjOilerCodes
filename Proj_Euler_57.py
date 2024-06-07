def Solve_Prob(n):
    answer = -1
    num = 1
    den = 1
    for i in range(1,n+1):
        a = num+2*den 
        b = num+den
        num = a
        den = b
        if len(str(num))>len(str(den)):
            print(i)
    return answer

# t = int(input())
t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    # print(answer)