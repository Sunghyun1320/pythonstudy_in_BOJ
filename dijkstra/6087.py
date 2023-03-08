import sys
input = sys.stdin.readline
import heapq
##############################################
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
##############################################
INF = int(1e9)
##############################################
w, h = map(int,input().split())

graph = [list(input().rstrip()) for _ in range(h)]


position = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == "C":
            position.append([i, j])


visit = []
x, y = position[0]
visited = [[INF for _ in range(w)] for _ in range(h)]
visited[x][y] = 0

dir_check = [[[False for _ in range(4)] for _ in range(w)] for _ in range(h)]

for dir in range(4):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 0 or nx >= h or ny < 0 or ny >= w or graph[nx][ny] == "*":
        continue

    visited[nx][ny] = 0
    dir_check[nx][ny][dir] = True
    heapq.heappush(visit, [0, nx, ny, dir])

while visit:
    count_mirror, x, y, dir = heapq.heappop(visit)

    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != "*":
        if visited[nx][ny] > count_mirror:
            visited[nx][ny] = count_mirror
            dir_check[nx][ny] = [False for _ in range(4)]
            dir_check[nx][ny][dir] = True
            heapq.heappush(visit, [count_mirror, nx, ny, dir])

        elif visited[nx][ny] == count_mirror:
            if dir_check[nx][ny][dir]:
                heapq.heappush(visit, [count_mirror, nx, ny, dir])
            dir_check[nx][ny][dir] = True

    nx = x + dx[(dir + 1) % 4]
    ny = y + dy[(dir + 1) % 4]

    if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != "*":
        if visited[nx][ny] > count_mirror + 1:
            visited[nx][ny] = count_mirror+1
            dir_check[nx][ny] = [False for _ in range(4)]
            dir_check[nx][ny][(dir + 1) % 4] = True
            heapq.heappush(visit, [count_mirror + 1, nx, ny, (dir+1) % 4])

        elif visited[nx][ny] == count_mirror + 1:
            if dir_check[nx][ny][(dir + 1) % 4]:
                heapq.heappush(visit, [count_mirror, nx, ny, (dir + 1) % 4])

            dir_check[nx][ny][(dir + 1) % 4] = True


    nx = x + dx[(dir - 1) % 4]
    ny = y + dy[(dir - 1) % 4]

    if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != "*":
        if visited[nx][ny] > count_mirror + 1:
            visited[nx][ny] = count_mirror+1
            dir_check[nx][ny] = [False for _ in range(4)]
            dir_check[nx][ny][(dir - 1) % 4] = True
            heapq.heappush(visit, [count_mirror+1, nx, ny, (dir-1) % 4])

        elif visited[nx][ny] == count_mirror + 1:
            if dir_check[nx][ny][(dir - 1) % 4]:
                heapq.heappush(visit, [count_mirror, nx, ny, (dir - 1) % 4])

            dir_check[nx][ny][(dir - 1) % 4] = True

print(visited[position[1][0]][position[1][1]])


