import sys

sys.stdin = open("9229.txt","r")

# N개의 봉지를 받는다
# 각 a 그램 의 무게를 가진다
# 최대의 양을 맞춰야하지만 M그램의 무개를 초과해서는 안된다


if __name__ == '__main__':
    T = int(input())

    for tc in range(T):

        N, M = map(int, input().split())

        arr = list(map(int, input().split()))

        max_weight = -1

        for i in range(N-1):
            for j in range(i+1, N):
                weight_sum = arr[i] + arr[j]
                if weight_sum <= M:
                    max_weight = max(max_weight, weight_sum)

        print("#{} {}".format(tc+1, max_weight))