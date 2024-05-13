import sys
sys.stdin = open("sin.txt", "r")

t = int(input())  # 총 테스트 케이스 개수
for tc in range(t):
     n, k = map(int, input().split())
     candy = list(map(int, input().split()))
     candy1 = sorted(candy)
     min_val = float('inf')
     for x in range(0, n):
         if x + (k - 1) < n:
             if min_val > candy1[x + (k - 1)] - candy1[x]:
                 min_val = candy1[x + (k - 1)] - candy1[x]
     print(f'#{tc+1} {min_val}')
