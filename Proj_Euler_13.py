ans = 0

def Solve_Prob(n):
    global ans
    ans = ans + n
    return ans

t = int(input())
for i in range(0,t):
    n = int(input())
    summ = Solve_Prob(n)

digit = len(str(summ))
answer = summ // (int(10**(digit-10)))
print(answer)