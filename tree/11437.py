import sys
input = sys.stdin.readline
#########################################
n = int(input())

node = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())

    node[b].append(a)
    node[a].append(b)

###################################################
def make_parents():
    visit = [1]
    visited = [0 for _ in range(n+1)]
    visited[1] = 1

    path = []

    while visit:
        now = visit.pop()

        # 이전에 방문한 노드이면
        # 자식노드 방문 완료, 현재 경로 저장 후 경로에서 현재 노드 삭제
        if visited[now] == 2:
            parents[now] = path.copy()
            path.pop()
            continue

        # 처음오는 노드이면 방문처리
        if visited[now] == 1:
            visited[now] += 1

        path.append(now)

        # 다시 돌아오기 위해 자기 자신을 넣어줌
        visit.append(now)
        for next_node in node[now]:
            if visited[next_node]:
                continue

            # visited에 1은 방문은 안햇지만, 방문예정이므로 따로 추가하지 않는다는 의미
            visited[next_node] = 1
            visit.append(next_node)


parents = [[] for _ in range(n+1)]
make_parents()
#############################################################
m = int(input())

for _ in range(m):
    a, b = map(int, input().split())

    len_a = len(parents[a])
    len_b = len(parents[b])

    i = 0
    j = 0

    while True:
        if i == len_a or j == len_b:
            print(parents[a][i-1])
            break

        if parents[a][i] != parents[b][j]:
            print(parents[a][i-1])
            break

        if parents[a][i] == parents[b][j]:
            i += 1
            j += 1






