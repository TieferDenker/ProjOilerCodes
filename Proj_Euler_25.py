from math import log10, floor

phi = 1.6180339887498948482045868343656381177203091798057628621354486227052604628189
sq5 = 2.2360679774997896964091736687312762354406183596115257242708972454

def Solve_Prob(n):
    i = 0
    while True:
        Fi = round(pow(phi,i)/sq5)
        # print(Fi)
        if Fi == 0:
            dig = 1
        else:
            dig = floor(log10(Fi))+1
        if dig == n:
            answer = i
            break 
        i=i+1
    return answer

t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)