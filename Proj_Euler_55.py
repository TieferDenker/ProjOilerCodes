def IsPalin(n):
    a = str(n)
    b = "".join(reversed(a))
    if a == b:
        return True
    else:
        return False

def Iterations(n):
    while True:
        a = str(n)
        b = "".join(reversed(a))
        n = n + int(b)
        if IsPalin(n):
            return n

def Solve_Prob(n):
    Iter = []
    answer = 0
    for i in range(1,n+1):
        Iter.append(Iterations(i))
    convergent = max(Iter,key=Iter.count)
    maxcount = Iter.count(convergent)
    print(convergent,maxcount)
    return answer

# t = int(input())
t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    # print(answer)