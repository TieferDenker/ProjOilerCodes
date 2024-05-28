Odd_Abun_Num = [945,1575,2205,2835,3465,4095,4725,5355,5775,5985,6435,6615,6825,7245,7425,7875,8085,8415,8505,8925,9135,9555,9765,10395,11025,11655,12285,12705,12915,13545,14175,14805,15015,15435,16065,16695,17325,17955,18585,19215,19305,19635,19845]
Sum_Small_Even_Abun = [24,30,32,36,38,40,42,44]
Even_Abun_Num = []
Summ_Abun = []

def Solve_Prob(n):
    if n > 20161:
        answer = "YES"
    else:
        if n%2 == 0:
            if n > 46:
                answer = "YES"
            else:
                if n in Sum_Small_Even_Abun:
                    answer = "YES"
                else:
                    answer = "NO"   
        else:
            if n < 957:
                answer = "NO"
            else:
                if n in Odd_Abun_Num_Sum:
                    answer = "YES"
                else:
                    answer = "NO"
    return answer

def IsAbun(n):
    summ = 0
    for i in range(1,n):
        if n%i == 0:
            summ = summ + i
    if summ > n:
        return True
    else:
        return False

N = 19217
for i in range(12,N,2):
    if IsAbun(i):
        Even_Abun_Num.append(i)

for i in Odd_Abun_Num:
    for j in Even_Abun_Num:
        x = i+j
        if x <= 20161:
            Summ_Abun.append(x)

Summ_Abun.sort
Odd_Abun_Num_Sum = set(Summ_Abun)
# print(Odd_Abun_Num_Sum)

q = int(input())
for i in range(0,q):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)