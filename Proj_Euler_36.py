def IsPalin(n):
    strr = str(n)
    for i in range(0, len(strr)//2): 
        if strr[i] != strr[len(strr)-i-1]: 
            return False
    return True

def ConvBase(n,k):
    st = ""
    while not(n == 0):
        st = st + str(n%k)
        n = n//k
    st = "".join(reversed(st))
    return int(st)

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
    n,k = map(int, input().split())
    answer = Solve_Prob(n,k)
    print(answer)