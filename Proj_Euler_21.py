def is_ami(n):
    count = 0
    counts = 0
    for i in range(1,n):
        if n%i == 0:
            count = count + i
    if not(count == n):
        for i in range(1,count):
            if count%i == 0:
                counts = counts + i
        if n == counts:
            return True
        else:
            return False
    else:
        return False 

def Solve_Prob(n):
    summ = 0
    for i in range(1,n):
        if is_ami(i):
            summ = summ + i
    answer = summ 
    return answer

t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)