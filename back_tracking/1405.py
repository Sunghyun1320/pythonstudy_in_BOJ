dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, *persent = map(int, input().split())


def cal(depth, n, x, y, per=1):
    if per == 0:
        return

    if depth == n:
        global answer
        answer += per
        return

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if visited[nx][ny]:
            continue

        visited[nx][ny] = True
        cal(depth+1, n, nx, ny, per*persent[dir])
        visited[nx][ny] = False


visited = [[False for _ in range(n*2+1)] for _ in range(n*2+1)]
visited[n][n] = True
answer = 0

cal(0, n, n, n)


for i in range(n):
    answer /= 100

print(answer)