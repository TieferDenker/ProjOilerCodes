def IsPalin(n):
    strr = str(n)
    for i in range(0, len(strr)//2): 
        if strr[i] != strr[len(strr)-i-1]: 
            return False
    return True

def IsPalinWithBase(n,k):
    if IsPalin(n):
        m = ConvBase(n,k)
        if IsPalin(m):
            return True
    return False

def Solve_Prob(n,k):
    summ = 0
    for i in range(1,n):
        if IsPalinWithBase(i,k):
            summ = summ + i
    answer = summ
    return answer

# t = int(input())
t = 1
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)