import sys
input = sys.stdin.readline
################################################
main_line = [i*2 for i in range(21)]
order_line_1 = [10, 13, 16, 19, 25]
order_line_2 = [20, 22, 24, 25]
order_line_3 = [30, 28, 27, 26, 25]
order_line_4 = [25, 30, 35, 40]
goal = [40]

line = [main_line, order_line_1, order_line_2, order_line_3, order_line_4, goal]

def dfs(point = 0, depth = 0):
    if depth == 10:
        global answer
        answer = max(answer, point)
        return

    order = dice[depth]

    for horse_num in range(4):
        if horse[horse_num][2]:
            continue

        now_position = [horse[horse_num][0],horse[horse_num][1]]

        horse[horse_num][1] += order

        if horse[horse_num][0] == 0 and horse[horse_num][0] == 5:
            horse[horse_num][0] = 1
            horse[horse_num][1] = 0

        elif horse[horse_num][0] == 0 and horse[horse_num][0] == 10:
            horse[horse_num][0] = 2
            horse[horse_num][1] = 0

        elif horse[horse_num][0] == 0 and horse[horse_num][0] == 15:
            horse[horse_num][0] = 3
            horse[horse_num][1] = 0

        elif horse[horse_num][0] == 0 and horse[horse_num][0] == 20:
            horse[horse_num][0] = 5
            horse[horse_num][1] = 0

        elif horse[horse_num][0] == 0 and horse[horse_num][0] > 20:
            horse[horse_num][0] = -1
            horse[horse_num][0] = -1
            horse[horse_num][2] = True

        elif horse[horse_num][0] != 0 and horse[horse_num][0] != 4 and horse[horse_num][0] != 5:
            if horse[horse_num][1] >= len(line[horse[horse_num][0]]):
                horse[horse_num][0] = 4
                horse[horse_num][1] -= len(line[horse[horse_num][0]])

        if horse[horse_num][0] == 4 and horse[horse_num][1] == 3:
            horse[horse_num][0] = 5
            horse[horse_num][1] = 0

        elif horse[horse_num][0] == 4 and horse[horse_num][1] > 3:
            horse[horse_num][0] = -1
            horse[horse_num][1] = -1
            horse[horse_num][2] = True

        if horse[horse_num][0] == 5 and horse[horse_num][1] > 0:
            horse[horse_num][0] = -1
            horse[horse_num][1] = -1
            horse[horse_num][2] = True


        check = False

        for i in range(4):
            if horse[i][2] or i == horse_num:
                continue

            if horse[i][0] == horse[horse_num][0] and horse[i][1] == horse[horse_num][1]:
                check = True

        if check:
            continue

        if horse[horse_num][2]:
            dfs(point, depth + 1)
        else:
            dfs(point + line[horse[horse_num][0]][horse[horse_num][1]], depth + 1)

        horse[horse_num][0] = now_position[0]
        horse[horse_num][1] = now_position[1]
        horse[horse_num][2] = False





dice = list(map(int, input().split()))

horse = [[0, 0, False], [0, 0, False], [0, 0, False], [0, 0, False]]
answer = 0
dfs()

print(answer)

