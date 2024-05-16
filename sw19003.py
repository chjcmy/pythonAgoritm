import sys

sys.stdin  = open("sw19003.txt", "r")

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())

    # 정답은 어떻게 될 지 모르겠더라고요. 그래서 0으로 해뒀습니다.
    # cnt는 나중에 씁니다.
    answer = cnt = 0

    # 팰린드롬 문자열이 있느냐 없느냐만 중요합니다.
    palindrome = False
    # 팰린드롬 문자열이 아닐 경우를 저장하는 리스트입니다.
    isNot = []

    # 이 곳에선 문자열을 받자마자 팰린드롬인지 판별합니다.
    # 만약 팰린드롬이 아니라면 isNot으로, 팰린드롬이면 그냥 True로 값을 바꿔줍니다.
    for _ in range(N):
        a = input().rstrip()
        if a != a[::-1]:
            isNot.append(a)
        else:
            palindrome = True

    # 여기선 isNot 리스트에 있는 문자열들을 걸러내고 cnt를 추가해줄겁니다.
    # 어차피 반대로 했을 때 맞는 요소가 있으면 한 쌍이라는 거니까 걍 2를 추가해줬습니다.
    for _ in range(len(isNot)):
        temp = isNot.pop()
        if temp[::-1] in isNot:
            cnt += 2

    ## 여기까지의 과정을 다 거치면 isNot에는 조건을 충족한 것들만 남고,
    ## palindrome은 True 혹은 False가 되겠죠

    # 만약 걸러낸 짝이 'ab', 'ba' 였다면 cnt는 2였을테고, 'abba', 'baab' 둘 다
    # 문자열 길이가 4입니다. ( cnt(2) * M(2) = 4 )
    answer = cnt * M

    # 만약 palindrome이 True라면 가운데 들어갈 수 있겠습니다.
    # 위의 예시대로라면 M은 2였을테니 palindrome이 'cc'였다면 'abccba'가 되겠죠.
    # 어차피 하나만 들어갈 수 있으니 M의 값을 한 번만 추가해줍니다.
    if palindrome:
        answer += M

    print(f'#{tc} {answer}')