def Solve_Prob(n,k,strm):
    maxi = -1
    for i in range(0,n-k+1):
        pro = 1
        for j in range(i,i+k):
            pro = pro*int(strm[j])
        if pro > maxi:
            maxi = pro
    answer = maxi
    return answer

t = int(input())
for i in range(0,t):
    n,k = list(map(int,input().split()))
    m = input()
    answer = Solve_Prob(n,k,m)
    print(answer)
