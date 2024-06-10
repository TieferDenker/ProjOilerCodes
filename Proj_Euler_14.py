COLSEQ = [-1]
MAXLEN = [-1]

def GenSeq(n):
    global COLSEQ
    for i in range(1,n+1):
        count = 1
        num = i
        while not(num == 1):
            if (num%2 == 0):
                num = num//2
            else:
                num = 3*num+1
            if len(COLSEQ)-1 >= num:
                count = count + COLSEQ[num]
                break
            else:
                count = count + 1
        COLSEQ.append(count)

def GenMaxLen(n):
    global COLSEQ
    global MAXLEN
    maxx = -1
    for i in range(1,n+1):
        x = COLSEQ[i]
        if x >= maxx:
            MAXLEN.append(i)
            last = i
            maxx = x
        else:
            MAXLEN.append(last)

def Solve_Prob(n):
    answer = MAXLEN[n]
    return answer

N = int(5*10E5)
# N = 100
GenSeq(N)
# print(COLSEQ)
GenMaxLen(N)
# print(MAXLEN)

t = int(input())
# t = 1
for i in range(0,t):
    # n,k = map(int, input().split())
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)