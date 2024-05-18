# 18662
import sys

sys.stdin = open('sw18662.txt', 'r')

if __name__ == '__main__':

    T = int(input())

    for tc in range(T):
        a, b, c = map(int, input().split())

        result = 0
        if a + c == 2 * b:
            print(f"#{tc + 1} {0.0}")
        else:
            if 2 * b > a + c:
                result = (2 * b) - (a + c)
                result /= 2
            elif 2 * b < a + c:
                result = (a + c) - (2 * b)
                result /= 2
            print(f"#{tc + 1} {result}")



