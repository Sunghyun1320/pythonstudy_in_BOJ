import sys
input = sys.stdin.readline
###########################################
n = int(input())

# 그래프 형태로 입력받기
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


###########################################
# 트리형태에서 부모노드와 자신의 레벨만 저장
tree = [0 for _ in range(n+1)]

visit = [1]
level = [0 for _ in range(n+1)]
level[1] = 1

while visit:
    now = visit.pop()

    for next_node in graph[now]:
        if level[next_node] != 0:
            continue

        level[next_node] = level[now] + 1
        tree[next_node] = now
        visit.append(next_node)


###########################################
m = int(input())

for _ in range(m):
    a, b = map(int, input().split())

    while True:
        if a == b:
            break

        if level[a] > level[b]:
            a = tree[a]
            continue

        else:
            b = tree[b]

    print(a)
