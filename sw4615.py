import sys

sys.stdin = open("4615.txt","r")

dx=[-1, 1, 0, 0, -1, -1, 1, 1]
dy=[0, 0, -1, 1, -1, 1, -1, 1]

def check(x, y, color):
    for i in range(8):
        nx, ny = x +dx[i], y + dy[i]
        temp = []
        while 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 0:
                break
            elif arr[nx][ny] == color:
                for tx, ty in temp:
                    arr[tx][ty] = color
                break
            else:
                temp.append((nx, ny))
            nx += dx[i]
            ny += dy[i]

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N//2-1][N//2-1] = arr[N//2][N//2] = 2
    arr[N//2-1][N//2] = arr[N//2][N//2-1] = 1

    for _ in range(M):
        x, y, color = map(int, input().split())
        arr[x-1][y-1] = color
        check(x-1, y-1, color)

    black = sum(arr[i][j] == 1 for i in range(N) for j in range(N))
    white = sum(arr[i][j] == 2 for i in range(N) for j in range(N))
    print(f"#{tc+1} {black} {white}")

