import sys

sys.stdin = open("sw6190.txt", "r")

# T값을 받는다
# n값을 받는다
# input.split을 통하여 값을 받는다
# max_num으로 -1으로 변수를 만든다
# i 부터 i-1 까지 for 문을 돌린다
# j(i+1) 부터 n 만큼 for문을 돌린다
# arr[i]와 arr[j]의 값을 곱한다
# 스트링으로 변경한다
# boolean 변수를 만든다
# 스트링의 갯수만큼 for문을 돌린다
# 만약, 단수가 아닐시에 False로 boolean을 만들고 break를 한다
# 만약 boolean 변수가 True이고 max_num 보다 크다면 max_num 을 새로운 변수로 만든다

if __name__ == '__main__':
    T = int(input())

    for tc in range(T):
        n = int(input())

        arr = list(map(int, input().split()))

        max_num = -1

        for i in range(n - 1):
            for j in range(i + 1, n):
                m_str = str(arr[i] * arr[j])

                check = True

                for k in range(len(m_str) - 1):
                    if m_str[k] > m_str[k + 1]:
                        check = False
                        break

                if check and max_num < int(m_str):
                    max_num = int(m_str)

        print("#{} {}".format(tc + 1, max_num))

