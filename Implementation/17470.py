from copy import deepcopy
import sys
input = sys.stdin.readline
##########################################
def cal_1(arr):
    if result[2] % 2 == 1:
        return cal_2(arr)

    for i in range(n//2):
        arr[n//2 - 1 - i], arr[n//2 + i] = arr[n//2 + i], arr[n//2 - 1 - i]

    result[0] += 1

    return deepcopy(arr)


##########################################
def cal_2(arr):
    if result[2] % 2 == 1:
        return cal_1(arr)

    for i in range(n):
        for j in range(m//2):
            arr[i][m//2 - 1 - j], arr[i][m//2 + j] = arr[i][m//2 + j], arr[i][m//2 - 1 - j]

        result[1] += 1

    return deepcopy(arr)


##########################################
def cal_3(arr):
    global n, m
    new_arr = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            new_arr[i][j] = arr[n-j-1][i]

    n, m = m, n

    result[2] = (result[2] + 1) % 4

    return new_arr


##########################################
def cal_4(arr):
    global n, m
    new_arr = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            new_arr[i][j] = arr[j][m - i - 1]

    n, m = m, n

    result[2] = (result[2] - 1) % 4

    return new_arr


##########################################
def cal_5(arr):
    new_arr = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n//2):
        for j in range(m//2):
            new_arr[i][j + m//2] = arr[i][j]

    for i in range(n//2):
        for j in range(m//2, m):
            new_arr[i + n//2][j] = arr[i][j]

    for i in range(n//2, n):
        for j in range(m//2):
            new_arr[i - n//2][j] = arr[i][j]

    for i in range(n//2, n):
        for j in range(m//2, m):
            new_arr[i][j - m//2] = arr[i][j]

    return new_arr

##########################################
def cal_6(arr):
    new_arr = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n//2):
        for j in range(m//2):
            new_arr[i + n//2][j] = arr[i][j]

    for i in range(n//2):
        for j in range(m//2, m):
            new_arr[i][j - m//2] = arr[i][j]

    for i in range(n//2, n):
        for j in range(m//2):
            new_arr[i][j + m//2] = arr[i][j]

    for i in range(n//2, n):
        for j in range(m//2, m):
            new_arr[i - n//2][j] = arr[i][j]

    return new_arr


##########################################
n1, m1, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n1)]
order = list(map(int, input().split()))


n = m = 2
sample_list = [[1, 2], [3, 4]]
fun_list = [0, cal_1, cal_2, cal_3, cal_4, cal_5, cal_6]

result = [0, 0, 0]

for i in range(r):
    sample_list = fun_list[order[i]](sample_list)

for i in sample_list:
    print(*i)
