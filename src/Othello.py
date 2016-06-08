sets = [[0 for i in range(8)] for i in range(8)]
dir_list = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

def init():
    for i in range(8):
        for j in range(8):
            sets[i][j] = 0
    sets[3][3] = 1
    sets[3][4] = 2
    sets[4][3] = 2
    sets[4][4] = 1


def turn(x, y, p):
    d_list = []
    change = []
    x -= 1
    y -= 1

    if sets[x][y] != 0:
        print("Can't input")
        return 1

    if p == 1:
        for i in range(8):
            d_x = x + dir_list[i][0]
            d_y = y + dir_list[i][1]

            if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                continue

            if sets[d_x][d_y] == 2:
                d_list.append(dir_list[i])
            else:
                continue

        if len(d_list) == 0:
            print("Can't input")
            return 1

        for i in range(len(d_list)):
            stack = []
            d_x = x + d_list[i][0]
            d_y = y + d_list[i][1]

            if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                continue

            while 1:
                stack.append((d_x, d_y))
                d_x += d_list[i][0]
                d_y += d_list[i][1]

                if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                    break

                if sets[d_x][d_y] == 1:
                    change = change + stack
                    break
                elif sets[d_x][d_y] == 0:
                    stack = []
                    break

        if len(change) == 0:
            print("Can't input")
            return 1

        while len(change) != 0:
            (a, b) = change.pop()
            sets[a][b] = 1
            if len(change) == 0:
                sets[x][y] = 1

    else:
        for i in range(8):
            d_x = x + dir_list[i][0]
            d_y = y + dir_list[i][1]

            if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                continue

            if sets[d_x][d_y] == 1:
                d_list.append(dir_list[i])
            else:
                continue

        if len(d_list) == 0:
            print("Can't input")
            return 1

        for i in range(len(d_list)):
            stack = []
            d_x = x + d_list[i][0]
            d_y = y + d_list[i][1]

            if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                continue

            while 1:
                stack.append((d_x, d_y))
                d_x += d_list[i][0]
                d_y += d_list[i][1]

                if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                    break

                if sets[d_x][d_y] == 2:
                    change = change + stack
                    break
                elif sets[d_x][d_y] == 0:
                    stack = []
                    break

        if len(change) == 0:
            print("Can't input")
            return 1

        while len(change) != 0:
            (a, b) = change.pop()
            sets[a][b] = 2
            if len(change) == 0:
                sets[x][y] = 2


def determine(p):
    con = 0

    for x in range(8):
        for y in range(8):
            d_list = []

            if sets[x][y] == 0:
                for i in range(8):
                    d_x = x + dir_list[i][0]
                    d_y = y + dir_list[i][1]

                    if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                        continue

                    if sets[d_x][d_y] != p and sets[d_x][d_y] != 0:
                        d_list.append(dir_list[i])

                for j in range(len(d_list)):
                    d_x = x + d_list[j][0]
                    d_y = y + d_list[j][1]

                    if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                        continue

                    while 1:
                        d_x += d_list[j][0]
                        d_y += d_list[j][1]

                        if d_x > 7 or d_x < 0 or d_y > 7 or d_y < 0:
                            break

                        if sets[d_x][d_y] == p:
                            con += 1
                            break
                        elif sets[d_x][d_y] == 0:
                            break

    if con == 0:
        return 1
    else:
        return 0


def finish():
    p_1 = 0
    p_2 = 0

    for i in range(8):
        for j in range(8):
            if sets[i][j] == 1:
                p_1 += 1
            elif sets[i][j] == 2:
                p_2 += 1

    if determine(1) == 1 and determine(2) == 1:
        if p_1 > p_2:
            print("Player1's Win!!")
        elif p_2 > p_1:
            print("Player2's Win!!")
        return 1

    if p_1 + p_2 > 63:
        if p_1 > p_2:
            print("Player1's Win!!")
        elif p_2 > p_1:
            print("Player2's Win!!")
        return 1


def __main__():
    init()
    n = 1

    for i in range(8):
        print(sets[i])

    while 1:
        if n % 2 == 1:
            n = 1
            t = determine(n)
        else:
            n = 2
            t = determine(n)

        if t == 1:
            print("Next turn")
            a += 1
            n += 1
            continue
        else:
            print("Player", n, "'s turn")
            x = int(input("Input x:"))
            y = int(input("Input y:"))
            tm = turn(y, x, n)

        if tm == 1:
            continue
        else:
            for i in range(8):
                print(sets[i])

            tmp = finish()
            n += 1
            if tmp == 1:
                print("Finish game")
                break


__main__()
