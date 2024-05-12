def Facto(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 24
    elif n == 5:
        return 120
    elif n == 6:
        return 720
    elif n == 7:
        return 5040
    elif n == 8:
        return 40320
    else:
        return 362880

def IsDesNum(n):
    m=n
    summ = 0
    while n>0:
        summ = summ + Facto(n%10)
        n = int(n/10)
    if summ%m == 0:
        return True
    else:
        return False

def Solve_Prob(n):
    summ = 0
    for i in range(10,n):
        if IsDesNum(i):
            summ = summ + i
    answer = summ
    return answer

# t = int(input())
t = 1
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)