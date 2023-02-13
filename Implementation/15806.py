import sys
input = sys.stdin.readline
###############################################
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
###############################################
# 곰팡이를 번식시키는 함수
def mold_breeding(mold):
    new_mold = []
    # new_room = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # 기존 곰팡이 모두 없애기
    for x, y in mold:
        room[x][y] = 0

    # 새 곰팡이 구하기
    for x, y in mold:
        # 8가지 방향에 대해서
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]

            # 범위 밖은 제외하고
            if nx <= 0 or nx > n or ny <= 0 or ny > n:
                continue

            # 비어있는 칸에 대해서 곰팡이 표시와, 새 곰팡이 추가
            if room[nx][ny] == 0:
                room[nx][ny] = 1
                new_mold.append([nx, ny])

    return new_mold

###############################################
n, m, k, t = map(int, input().split())

mold = [list(map(int, input().split())) for _ in range(m)]
room = [[0 for _ in range(n+1)] for _ in range(n+1)]

for x, y in mold:
    room[x][y] = 1

check_area = [list(map(int, input().split())) for _ in range(k)]

# 청소 검사 날짜 까지 곰팡이 번식 반복
for _ in range(t):
    mold = mold_breeding(mold)

# 체크영역에서 곰팡이 있으면 yes출력후 python종료
for x, y in check_area:
    if room[x][y] == 1:
        print("YES")
        exit()

# 곰팡이 영역없어서 python종료가 안되었다면, no출력
print("NO")

