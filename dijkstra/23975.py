import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
#################################################
n, m, k = map(int, input().split())

market = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append([b, c])
    graph[b].append([a, c])

visit = []
heapq.heappush(visit, [0, 1])

distance = [[INF, 0] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visited[1] = True
distance[1][0] = 0


while visit:
    cost, node = heapq.heappop(visit)

    for next_node, dis in graph[node]:
        if dis + cost < distance[next_node][0]:
            distance[next_node][0] = dis + cost
            distance[next_node][1] = node

        elif dis + cost == distance[next_node][0]:
            if distance[next_node][1] < node:
                distance[next_node][1] = node

        if visited[next_node]:
            continue

        visited[next_node] = True
        heapq.heappush(visit, [dis+cost, next_node])


for _ in range(k):
    now_mart = int(input())
    if distance[now_mart][0] == INF:
        print(-1)
        continue

    while True:
        if now_mart == 0:
            break

        if market[now_mart] > 0:
            market[now_mart] -= 1
            print(now_mart)
            break

        now_mart = distance[now_mart][1]

    if now_mart == 0:
        print(-1)




