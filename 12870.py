import sys

if __name__ == '__main__':
    N = int(input())

    arr = list(map(int, input().split()))

    sorted_arr = sorted(set(arr))
    rank_dic = {val : idx for idx, val in enumerate(sorted_arr)}

    result = [rank_dic[val] for val in arr]
    print(*result, sep=' ')