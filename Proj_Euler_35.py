CircPri = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331]

def Solve_Prob(n):
    summ = 0
    for i in range(0,len(CircPri)):
        if CircPri[i] < n:
            summ = summ + CircPri[i]
        else:
            break
    answer = summ
    return answer

# t = int(input())
t = 1
for i in range(0,t):
    n = int(input())
    answer = Solve_Prob(n)
    print(answer)