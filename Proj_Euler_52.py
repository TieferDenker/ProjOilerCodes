def f(n,k):
    arr = [n]
    l = len(str(n))
    s = sorted(str(n))
    for i in range(2,k+1):
        x = len(str(n*i))
        y = sorted(str(n*i))
        if (l==x) and (s==y):
            arr.append(n*i)
        else:
            return False,arr
    return True,arr 

def Solve_Prob(n,k):
    answer = 0
    for i in range(125874,n+1):
        flag,mult = f(i,k)
        if flag:
            for j in mult:
                print(j,end=" ")
            print("")
    return answer

# t = int(input())
t = 1
for i in range(0,t):
    n,k = map(int, input().split())
    # n = int(input())
    answer = Solve_Prob(n,k)
    # print(answer)