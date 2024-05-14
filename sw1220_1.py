import sys

sys.stdin = open("1220.txt", "r")


def count_interaction(arr):
    count = 0

    for j in range(100):
        north_flag= False

        for i in range(100):
            if arr[i][j] == 1:
                north_flag = True
            elif arr[i][j] == 2 and north_flag:
                count += 1
                north_flag = False

    return count


if __name__ == '__main__':


    T = 10

    for tc in range(T):
        N = int(input())

        arr = [list(map(int, input().split())) for _ in range(100)]

        result = count_interaction(arr)

        print("#{} {}".format(tc+1, result))