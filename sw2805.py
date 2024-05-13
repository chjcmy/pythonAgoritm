import sys

sys.stdin = open('sw2805.txt', 'r')

if __name__ == '__main__':

    T = int(input())

    for testCase in range(1, T + 1):
        N = int(input())
        farm = [list(map(int, input())) for _ in range(N)]  # 농장 정보
        startIndex = N // 2  # 첫 번째로 계산할 땅의 세로 위치
        size = 1  # 계산할 땅의 개수
        result = 0
        for i in range(N):
            for j in range(startIndex, startIndex + size):
                result += farm[i][j]
            if i < N // 2:
                startIndex -= 1
                size += 2
            else:
                startIndex += 1
                size -= 2
        print(f"#{testCase} {result}")