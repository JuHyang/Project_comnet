view[8][8] = {0}
sets[8][8] = {0}
dic[8] = {0}


def input(int x, int y, int p):
    dic[8] = {0}

    if p == 1:
        e = input_m(x, y, p)

        if e == 0:
            print "놓을 수 없는 자리입니다."
            return 0

        else:
            e = input_m2(x, y, p)

            if e == 0:
                print "놓을 수 없는 자리입니다."
                return 0

            else:

    else:

def input_m1(int x, int y, int p):

    if p == 1:

        if sets[x - 1][y - 1] == 2:
            dic[0] = 1

        else if sets[x][y - 1] == 2:
            dic[1] = 1

        else if sets[x + 1][y - 1] == 2:
            dic[2] = 1

        else if sets[x + 1][y] == 2:
            dic[3] = 1

        else if sets[x + 1][y + 1] == 2:
            dic[4] = 1

        else if sets[x][y + 1] == 2:
            dic[5] = 1

        else if sets[x - 1][y + 1] == 2:
            dic[6] = 1

        else if sets[x - 1][y] == 2:
            dic[7] = 1

    else:

        if sets[x - 1][y - 1] == 1:
            dic[0] = 1

        else if sets[x][y - 1] == 1:
            dic[1] = 1

        else if sets[x + 1][y - 1] == 1:
            dic[2] = 1

        else if sets[x + 1][y] == 1:
            dic[3] = 1

        else if sets[x + 1][y + 1] == 1:
            dic[4] = 1

        else if sets[x][y + 1] == 1:
            dic[5] = 1

        else if sets[x - 1][y + 1] == 1:
            dic[6] = 1

        else if sets[x - 1][y] == 1:
            dic[7] = 1

    for i in range(0, len(dic)):

        if not dic[i] == 0:
            return 1

        if i == len(dic) - 1:
            return 0

def input_m2(int x, int y, int p):
    if p == 1:

        for i in range(0,len(dic)):

            if dic[i] == 1:

                while x != 0:
                    x -= 1
                    if sets[x][y] == 1:
                        dic[i] = 2
                        return 1
                        
