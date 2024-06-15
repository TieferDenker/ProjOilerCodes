from math import log10

phi = 1.6180339887498948482045868343656381177203091798057628621354486227052604628189
sq5 = 2.2360679774997896964091736687312762354406183596115257242708972454

def Solve_Prob(n):
    a = log10(sq5)
    b = n-1
    c = log10(phi)
    answer = 1+int((a+b)/c)
    return answer

t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)