import sys

sys.stdin = open("sw3431.txt", "r")

if __name__ == '__main__':
    T = int(input())

    for tc in range(T):
        min_t, max_t, him = map(int, input().split())

        ans = -1

        if min_t > him:
            ans = min_t - him
        elif min_t <= him <= max_t:
            ans = 0

        print("#{} {}".format(tc+1, ans))