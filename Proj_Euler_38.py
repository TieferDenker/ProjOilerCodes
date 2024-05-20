def Solve_Prob(n):
    for i in range(1,n+1):
        z = i
        count = 0
        if i%2 == 1:
            count = 0
        else:
            a = i//2
            for k in range(1,a+1):
                if a%k == 0:
                    m = k
                    n = (a//k) - k
                    if m>0 and n>0 and m>n:
                        count = count + 1
        if count > 0:
            print(z,count)
    # return answer

# t = int(input())
t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    # answer = Solve_Prob(n)
    Solve_Prob(n)
    # print(answer)