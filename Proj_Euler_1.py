t = int(input())
for i in range(0,t):
    n = int(input())
    n = n - 1
    a = int(n//3)
    b = int(n//5)
    c = int(n//15)
    s1 = 3*a*(a+1)//2
    s2 = 5*b*(b+1)//2
    s3 = 15*c*(c+1)//2
    answer = s1 + s2 - s3
    print(int(answer))