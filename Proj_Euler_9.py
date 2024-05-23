import itertools, math

n = 3000
# n = 100
answers = [-1]*(2*n+1)

for item in itertools.combinations(range(1,int(n**0.5)+1,2),r = 2): 
    t = item[0]
    s = item[1]
    if math.gcd(s,t) == 1:
        k = 1
        for i in range(s*(s+t),n+1,s*(s+t)):
            abc = (s*t*(s**4-t**4))//4
            abc = abc*k*k*k
            answers[i] = max(answers[i],abc)
            k = k + 1
# print(answers)

def Solve_Prob(n):
    answer = answers[n]
    return answer
    
t = int(input())
# t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)
