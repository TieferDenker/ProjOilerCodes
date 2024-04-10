eps = 0.000000000000000001

def Solve_Prob(n,k,strm):
    res = [int(x) for x in strm]
    pro = 1
    for i in range(0,n):
        if res[i] == 0:
            res[i] = eps
    for i in range(0,k):
        pro = pro * res[i]
    maxi = pro
    i = 0
    while i < (n-k):
        pro = (pro / res[i]) * res[i+k]
        if pro > maxi:
            maxi = pro
        i = i + 1
    answer = int(maxi)
    return answer

t = int(input())
for i in range(0,t):
    n,k = list(map(int,input().split()))
    m = input()
    answer = Solve_Prob(n,k,m)
    print(answer)
