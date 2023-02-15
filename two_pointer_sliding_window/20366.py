import sys
input = sys.stdin.readline
##########################################
n = int(input())

snow = list(map(int, input().split()))

snow.sort()

answer = int(10e9)
for i in range(n - 3):
    for j in range(i+3, n):
        check = snow[j] + snow[i] - snow[i+1] - snow[i+2]
        check = check if check > 0 else -check
        answer = min(answer, check)

        check = snow[j] + snow[i] - snow[i + 1] - snow[j - 1]
        check = check if check > 0 else -check
        answer = min(answer, check)

        check = snow[j] + snow[i] - snow[j - 1] - snow[j - 2]
        check = check if check > 0 else -check
        answer = min(answer, check)

print(answer)