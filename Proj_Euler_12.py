TRI = [1, 3, 6, 28, 36, 120, 300, 528, 630, 2016, 3240, 5460, 25200, 73920, 157080, 437580, 749700, 1385280, 1493856, 2031120, 2162160, 17907120, 76576500, 103672800, 236215980, 842161320]
DIV = [1, 2, 4,  6,  9,  16,  18,  20,  24,   36,   40,   48,    90,   112,    128,    144,    162,     168,     192,     240,     320,      480,      576,       648,       768,      1024]

def Solve_Prob(n):
    left, right = 0, len(DIV) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if DIV[mid] <= n:
            left = mid + 1
        else:
            right = mid - 1
            index = mid

    answer = TRI[index]
    return answer

t = int(input())
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)
