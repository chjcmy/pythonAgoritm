import sys

#N개의 과자 봉지를 담는다
#무게를 저장 한다
#M 그램을 저장한다
#맥스 무게를 -1 로 둔다
#처음부터 하나씩 다 더해본다
#max 무게 보다 더 무거울 경우 max 무게를 저장한다
#max 무게를 출력한다

sys.stdin = open("9229.txt", "r")

if __name__ == '__main__':
    T = int(input())

    for tc in range(T):
        N, M = map(int, input().split())
        snacks = list(map(int, input().split()))
        max_weight = -1

        for i in range(N-1):
            max_weight2 = snacks[i]
            for j in range(i+1,N):
                 max_weight2 += snacks[j]
                 if max_weight < max_weight2 and max_weight2 < M:
                     max_weight = max_weight2

        print("#{} {}".format(tc+1, max_weight))


