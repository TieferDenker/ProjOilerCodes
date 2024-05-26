def Solve_Prob(n):
    score1 = 0
    for i in range(0,len(n)):
        score1 = score1 + (ord(n[i])-64) # check this line
    # print(score1)
    k = 1
    for i in Words:
        if i == n:
            score2 = k
            break
        k = k + 1
    # print(score2)
    answer = score1*score2
    return answer

Words = []
t = int(input())
for i in range(0,t):
    n = input()
    Words.append(n)

Words.sort()

q = int(input())
for i in range(0,q):
    n = input()
    answer = Solve_Prob(n)
    print(answer)