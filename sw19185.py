import sys

sys.stdin = open("sw19185.txt", "r")

T = int(input())

if __name__ == '__main__':


    for tc in range(T):
        N, M = map(int, input().split(" "))

        arrN = list(map(str, input().split(" ")))
        arrM = list(map(str, input().split(" ")))

        cnt = int(input())

        ans = "#{} ".format(tc+1)

        for i in range(cnt):
            a = int(input())
            first = arrN[a % N - 1] + arrM[a % M - 1] + " "

            ans += first

        print(ans)