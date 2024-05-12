import sys

sys.stdin = open('sw2806.txt', 'r')

t = input()

for tc in range(t):
    n = int(input())

n = int(input())  # 체스판 크기 N
ans = 0
row = [0] * n  # 각 행에 퀸의 위치를 기록하는 배열

def is_promising(x):
    """
    현재 위치 (x, row[x])에 퀸을 놓을 수 있는지 확인하는 함수
    """
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            # (x, i) 위치에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)

n_queens(0)
print(ans)

