def Solve_Prob(n):
    if n%2 == 0:

        m = n//2
        k = 1
        maxi = -1
        while (k >= 1):
            if (m%k == 0):
                p = k
                q = (m//k)-k
                print(p,q)
                if (p > q) and (q >= 1):
                    a = p**2-q**2
                    b = 2*p*q
                    c = p**2+q**2
                    pro = a*b*c
                    if pro > maxi:
                        maxi = pro
            k = k + 1
        answer = maxi
    else:
        answer = -1
    return answer

t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)
