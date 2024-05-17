import sys

sys.stdin = open("1876.txt","r")

move_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

command_dict = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'S': 4,
                '^': 0, 'v': 1, '<': 2, '>': 3, 0: '^', 1: 'v', 2: '<', 3: '>'}

search_list = ['<','>','v','^']

if __name__ == '__main__':
    T = int(input())

    for tc in range(T):
        H, W = map(int, input().split())

        tank_pos = None  # tank_pos 초기화

        arr = [list(input()) for _ in range(H)]

        for i in range(H):
            for j in range(W):
                for target in range(4):
                    if arr[i][j] in search_list:
                        tank_pos = (i, j, command_dict[arr[i][j]])
                        break
                else: continue
                break

        input()

        commands = input()

        for command in commands:
            temp = command_dict[command]

            if temp == 4:
                dy = tank_pos[0]
                dx = tank_pos[1]

                while True:
                    dy += move_list[tank_pos[2]][0]
                    dx += move_list[tank_pos[2]][1]

                    if 0 > dy or dy >= H or 0 > dx or dx >= W or arr[dy][dx] == '#':
                        break

                    if arr[dy][dx] == '*':
                        arr[dy][dx] = '.'
                        break

            else:
                y = tank_pos[0]
                x = tank_pos[1]
                dy = y + move_list[temp][0]
                dx = x + move_list[temp][1]
                arr[x][y] = command_dict[temp]
                tank_pos = (y, x, temp)

                if 0 <= dy < H and 0 <= dx < W and arr[dy][dx] == '.':
                    arr[y][x] = '.'
                    arr[dy][dx] = command_dict[temp]
                    tank_pos = (dx, dy, temp)

        print('#{}'.format(tc+1), end = '')
        for m in arr:
            print(''.join(m))