def FindMax(B):
    k = 4
    l = len(B)
    maxx = -1
    if l-k+1 > 0:
        for i in range(0,l-k+1):
            prod = 1
            for j in range(i,i+k):
                prod = prod*B[j]
            maxx = max(maxx,prod)
    return maxx

def Solve_Prob(A):
    maxx = -1
    for i in range(0,rows):
        maxx = max(maxx,FindMax(A[i]))
    for j in range(0,cols):
        B = []
        for i in range(0,rows):
            B.append(A[i][j])
        maxx = max(maxx,FindMax(B))

    for j in range(0,cols):
        B = []
        for i in range(0,j+1):
            B.append(A[i][j-i])
        maxx = max(maxx,FindMax(B))
    for j in range(cols,2*cols-1):
        B = []
        for i in range(0,2*cols-j-1):
            B.append(A[rows-1-i][j-rows+1+i])
        maxx = max(maxx,FindMax(B))

    for j in range(0,cols):
        B = []
        for i in range(0,cols-j):
            B.append(A[j+i][i])
        maxx = max(maxx,FindMax(B))
    for j in range(0,cols-1):
        B = []
        for i in range(j,cols-1):
            B.append(A[i-j][i+1])
        maxx = max(maxx,FindMax(B))
    answer = maxx
    return answer

cols = 20
rows = 20
A = [[0]*cols]*rows

for i in range(0,rows): 
    A[i] = list(map(int,input().split()))
answer = Solve_Prob(A)
print(answer)