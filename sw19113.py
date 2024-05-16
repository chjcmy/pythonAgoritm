# 4의 배수로 할인 해보고 맞다면 배열에 추가
import sys
sys.stdin = open("19113.txt","r")

if __name__ == '__main__':
    T = int(input())

    for tc in range(T):
        N = int(input())
        price_lst = list(map(int, input().split()))

        price = []
        while price_lst:
            for i in range(len(price_lst)):
                if price_lst[i] % 4 == 0 and int(price_lst[i] * (3 / 4)) in price_lst:
                    a = price_lst.pop(i)
                    idx = price_lst.index(int(a * (3 / 4)))
                    b = price_lst.pop(idx)

                    price.append(b)
                    break

        res = " ".join(list(map(str, price)))
        print(f"#{tc + 1} {res}")


