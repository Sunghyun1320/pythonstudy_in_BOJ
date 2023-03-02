import sys
input = sys.stdin.readline
from collections import deque
##################################################
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
##################################################
r, c = map(int, input().split())

lack = [list(input().rstrip()) for _ in range(r)]
water = deque()
swan = deque()
temp = deque()
visited = [[False for _ in range(c)] for _ in range(r)]
##################################################
def melt_ice():
    while water:
        x, y = water.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if nx < 0 or nx >= r or ny < 0 or ny >= c or lack[nx][ny] != "X":
                continue

            lack[nx][ny] = "."
            temp.append([nx, ny])

##################################################
def check_meet():
    while swan:
        x, y = swan.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if nx < 0 or nx >= r or ny < 0 or ny >= c or visited[nx][ny]:
                continue

            visited[nx][ny] = True

            if lack[nx][ny] == "X":
                temp.append([nx, ny])

            elif lack[nx][ny] == ".":
                swan.append([nx, ny])

            elif lack[nx][ny] == "L":
                return True

    return False


##################################################
# 물과 백조의 위치를 저장
for i in range(r):
    for j in range(c):
        if lack[i][j] != "X":
            water.append([i, j])

        if not swan and lack[i][j] == "L":
            swan.append([i, j])
            visited[i][j] = True

##################################################
day = 0
while True:
    if check_meet():
        print(day)
        break
    swan = temp
    temp = deque()
    melt_ice()
    water = temp
    temp = deque()
    day += 1





