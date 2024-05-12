import sys

sys.stdin = open('20551.txt', 'r')

def find_longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # 각 위치에서 가장 긴 증가하는 부분 수열의 길이를 저장하는 리스트

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

t = int(input())

for tc in range(t):
    box_numbers = list(map(int, input().split()))  # 상자에 들어있는 사탕의 개수
    result = find_longest_increasing_subsequence(box_numbers)
    print(result)