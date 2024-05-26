import sys

sys.stdin = open("3499.txt","r")

if __name__ == '__main__':
    T = int(input())

    for tc in range(T):
        N = int(input())

        half_n = N // 2

        if(N % 2 == 1):
            half_n = N // 2 + 1

        arr = list(map(str, input().split()))

        ans = "#{} ".format(tc+1)

        for i in range(half_n):
            ans += "{} ".format(arr[i])

            if N % 2 == 1 and i + 1 == half_n:
                break
            else:
                ans += "{} ".format(arr[half_n+i])

        print(ans)
