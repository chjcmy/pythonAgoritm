import heapq

def dijkstra(graph, start):
    distances = [float('inf')] * (len(graph) + 1)
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node] :
            continue
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                distances[neighbor] = distances[node] + weight
                heapq.heappush(heap, (distances[neighbor], neighbor))

        return distances

def solve():
    n, e = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    v1, v2 = map(int, input().split())

    dist_from_1 = dijkstra(graph, 1)

    result = min(dist_from_1[v1] + dijkstra(graph, v1)[v2] + dijkstra(graph, v2)[n],
                 dist_from_1[v2] + dijkstra(graph, v2)[v1] + dijkstra(graph, v1)[n])

    if result == float('inf'):
        print(-1)
    else:
        print(result)


solve()