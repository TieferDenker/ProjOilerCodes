def Solve_Prob(n):
    i = 1
    while True:
        m = pow(i,n)
        dig = len(str(m))
        if (dig == n):
            print(m)
        elif (dig > n):
            break
        i += 1

# t = int(input())
t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    # print(answer)
