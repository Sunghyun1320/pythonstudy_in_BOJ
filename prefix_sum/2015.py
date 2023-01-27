import sys
input = sys.stdin.readline
#############################################
n, k = map(int, input().split())

sum_ = [0 for _ in range(n+1)]

sum_temp = 0
data = list(map(int, input().split()))
for i in range(1, n+1):
    sum_temp += data[i-1]
    sum_[i] = sum_temp




