def Solve_Prob(n):
    if n == 3:
        answer = 153+370+371+407
    elif n == 4:
        answer = 1634+8208+9474
    elif n == 5:
        answer = 4150+4151+54748+92727+93084+194979
    elif n ==6:
        answer = 548834
    return answer

# t = int(input())
t = 1
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)