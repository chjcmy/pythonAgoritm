import sys

sys.stdin = open("2814.txt", "r")

def dfs(node, visited):
    global max_length
    visited[node] = True
    length = sum(visited)
    if length > max_length:
        max_length = length
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, visited)
    visited[node] = False

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    max_length = 0
    for node in range(1, N + 1):
        dfs(node, [False] * (N + 1))
    print(f"#{test_case} {max_length}")