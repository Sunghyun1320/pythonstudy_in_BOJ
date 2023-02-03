import sys
input = sys.stdin.readline
######################################
n = int(input())

paper = [[0 for _ in range(101)] for _ in range(101)]

min_v = 100
max_v = 0
min_h = 100
max_v = 0

for _ in range(n):
    a, b = map(int, input())

    min_v = min_v if a > min_v else a
    min_h = min_h if b > min_h else b
    max_v = max_v if a < max_v else a
    max_h = max_h if b < max_h else b

    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] = 1

sum_h = [[0 for _ in range(max_v - min_v)] for _ in range(max_h - min_h)]
sum_v = [[0 for _ in range(max_v - min_v)] for _ in range(max_h - min_h)]
