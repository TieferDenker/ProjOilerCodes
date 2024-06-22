def isdesinum(n):
    if n%4 == 0:
        return False
    if n%2 == 0:
        n = n//2

    for i in range(3,int(n**0.5)+1,2):
        if n%(i**2) == 0:
            return False
        if (n%i == 0) and (i%4 == 1):
            while n%i == 0:
                n = n//i
    if n>2:
        if n%4 == 1:
            return True
        else:
            return False
    return True

def Solve_Prob(n):
    count = 0
    for i in range(2,n+1):
        x = int(i**0.5) 
        if not(i == x**2):
            if isdesinum(i):
                count += 1
    answer = count
    return answer

# t = int(input())
t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)