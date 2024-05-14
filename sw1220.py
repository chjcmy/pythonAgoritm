import sys

sys.stdin = open('1220.txt', 'r')

def count_interactions(magnets):
    interactions = 0

    for j in range(100):
        flag_north = False

        for i in range(100):
            if magnets[i][j] == 1:
                flag_north = True
            elif magnets[i][j] == 2 and flag_north:
                interactions += 1
                flag_north = False

    return interactions




if __name__ == '__main__':

    for tc in range(10):
        N = int(input())

        magnets = [list(map(int, input().split())) for _ in range(100)]

        result = count_interactions(magnets)

        print("#{} {}".format(tc+1, result))

