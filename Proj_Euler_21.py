AMINUM = [220,284,1184,1210,2620,2924,5020,5564,6232,6368,10744,10856,12285,14595,17296,18416,63020,66928,66992,67095,69615,71145,76084,79750,87633,88730]   
AMISUM = [-1]

def GenSumAmi(n):
    global AMINUM
    global AMISUM
    summ = 0
    for i in range(1,n):
        if i in AMINUM:
            summ = summ + i
        AMISUM.append(summ)

def Solve_Prob(n):
    answer =  AMISUM[n]
    return answer

N = int(10E4)
GenSumAmi(N)

t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)