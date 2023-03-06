import sys
input = sys.stdin.readline
import heapq
######################################################
INF = int(sys.maxsize)
######################################################
n, m, k = map(int, input().split())

city = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())

    city[a].append([b, cost])
    city[b].append([a, cost])

distance = [INF for _ in range(n+1)]
distance[1] = 0

visit = []
heapq.heappush(visit, [0, 1, 0, INF])

while visit:
    new_cost, node, cover, cover_cost = heapq.heappop(visit)

    for next_node, cost in city[node]:
        if cover < k:
            n_cost = new_cost
            n_cover_cost = min(cover_cost, cost)

        else:
            n_cost = new_cost + min(cover_cost, cost)
            n_cover_cost = max(cover_cost, cost)

        if distance[next_node] <= n_cost:
            continue

        distance[next_node] = n_cost
        heapq.heappush(visit, [n_cost, next_node, cover + 1, n_cover_cost])

print(distance[n])
