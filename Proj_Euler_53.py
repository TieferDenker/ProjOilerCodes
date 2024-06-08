def Solve_Prob(n,k):
    count = 0
    for i in range(2,n+1):
        x = i
        for r in range(1,(n//2)+1):
            if x > k:
                count = count + (i-2*r+1)
                break
            x = (x*(i-r))//(r+1)
    answer = count
    return answer

# t = int(input())
t = 1
for i in range(0,t):
    n,k = map(int, input().split())
    # n = int(input())
    answer = Solve_Prob(n,k)
    print(answer)