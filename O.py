view = [[0 for i in range(8)] for i in range(8)]
sets = [[0 for i in range(8)] for i in range(8)]
dir_list = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

def init():
    sets[3][3] = 1
    sets[3][4] = 2
    sets[4][3] = 2
    sets[4][4] = 1

def input(x, y, p):
    d_list = []
    x -= 1
    y -= 1
    if p == 1:
        for i in range(8):
            d_x = x + dir_list[i][0]
            d_y = y + dir_list[i][1]
            if sets[d_x][d_y] == 2:
                d_list.append(dir_list[i])
            else:
                continue

        if len(d_list) == 0:
            print "Can't input"
            return 1

        for i in range(len(d_list)):
            stack = []
            d_x = x + d_list[i][0]
            d_y = y + d_list[i][1]
            while 1:
                stack.append((d_x, d_y))
                d_x += d_list[i][0]
                d_y += d_list[i][1]
                if sets[d_x][d_y] == 1:
                    break
                elif sets[d_x][d_y] == 0:
                    stack = []
                    break
            while len(stack) != 0:
                (a, b) = stack.pop()
                sets[a][b] = 1
        sets[x][y] = 1

    else:
        for i in range(8):
            d_x = x + dir_list[i][0]
            d_y = y + dir_list[i][1]
            if sets[d_x][d_y] == 1:
                d_list.append(dir_list[i])
            else:
                continue

        if len(d_list) == 0:
            print "Can't input"
            return 1

        for i in range(len(d_list)):
            stack = []
            d_x = x + d_list[i][0]
            d_y = y + d_list[i][1]
            while 1:
                stack.append((d_x, d_y))
                d_x += d_list[i][0]
                d_y += d_list[i][1]
                if sets[d_x][d_y] == 2:
                    break
                elif sets[d_x][d_y] == 0:
                    stack = []
                    break
            while len(stack) != 0:
                (a, b) = stack.pop()
                sets[a][b] = 2
        sets[x][y] = 2

def determine(p):
    stack = []

    for i in range(8):
        for j in range(8):
            if sets[i][j] == p:
                for k in range(8):
                    d_x = i + dir_list[k][0]
                    d_y = j + dir_list[k][1]
                    if sets[d_x][d_y] == 0:
                        stack.append((d_x, d_y))
    if len(stack) == 0:
        print "Next turn"
    else:
        print stack



init()
for i in range(8):
    print sets[i]
print "\n"
input(4, 3, 2)
determine(1)
input(3, 5, 1)
determine(2)
for i in range(8):
    print sets[i]
