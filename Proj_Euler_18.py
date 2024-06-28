def Solve_Prob(A):
    for i in range(len(A)-2,-1,-1):
        l = len(A[i])
        for j in range(0,l):
            A[i][j] = A[i][j]+max(A[i+1][j],A[i+1][j+1])
    return A[0][0]

t = int(input())
for i in range(0,t):
    n = int(input())
    A = []
    for j in range(0,n):
        x = []
        x = list(map(int, input().split()))
        A.append(x)
    answer = Solve_Prob(A)
    print(answer)
