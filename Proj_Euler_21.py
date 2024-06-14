Ami = []

def is_ami(n):
    count = 1
    counts = 1
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            count = count + i + n//i
    if not(count == n):
        for i in range(2,int(count**0.5)+1):
            if count%i == 0:
                counts = counts + i + count//i
        if n == counts:
            return True
        else:
            return False
    else:
        return False 

def GenAmi(n):
    for i in range(1,n):
        if is_ami(i):
            Ami.append(i)

def Solve_Prob(n):
    summ = 0
    for i in Ami:
        if i < n:
            summ = summ + i
    answer = summ
    return answer

t = int(input())
inputs = []
for i in range(0,t):
    n = int(input())
    inputs.append(n)

GenAmi(max(inputs))

for i in inputs:
    answer = Solve_Prob(i)
    print(answer)
