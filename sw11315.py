#11315

import sys

sys.stdin = open("11315.txt", "r")


def check():
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for dir in range(4):
                    nx = i
                    ny = j
                    cnt = 0
                    while 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[dir]
                        ny += dy[dir]
                    if cnt >= 5:
                        return 'YES'

    return 'NO'

if __name__ == '__main__':
    T = int(input())

    for tc in range(1, T + 1):
        n = int(input())
        arr = [input() for _ in range(n)]
        print('#%d %s' % (tc, check()))