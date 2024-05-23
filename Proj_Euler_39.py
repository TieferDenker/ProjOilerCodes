def Solve_Prob(n):
    if n < 60:
        answer = 12
    else:
        maxx = -1
        for i in range(60,n+1,60):
            count = 0
            for a in range(1,i+1):
                for b in range(a,i+1):
                    c = i - a - b
                    if a**2+b**2==c**2:
                        count = count+1
                        # print(i,a,b,c)   
            if count > maxx:
                maxx = count
                answer = i
                # print(answer)
    return answer

t = int(input())
# t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)