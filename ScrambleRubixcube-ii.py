def RightCW(x):  # action 9 Front right clock wise

    x[9:12, 0:3] = np.fliplr(x[9:12, 0:3].transpose())
    temp1 = np.array(x[0:3, 2])
    temp2 = np.array(x[12:15, 0])
    temp3 = np.array(x[15:18, 2])
    temp4 = np.array(x[6:9, 2])
    x[0:3, 2] = temp4
    x[12:15, 0] = np.fliplr([temp1])[0]
    x[15:18, 2] = np.fliplr([temp2])[0]
    x[6:9, 2] = temp3

def RightACW(x):  # action 10
    RightCW(x)
    RightCW(x)
    RightCW(x)

def BackCW(x):  # action 11 Front  back clock wise

    x[12:15, :] = np.fliplr(x[12:15, :].transpose())
    temp1 = np.array(x[0, 0:3])
    temp2 = np.array(x[3:6, 0])
    temp3 = np.array(x[17, 0:3])
    temp4 = np.array(x[9:12, 2])
    x[0, 0:3] = temp4
    x[3:6, 0] = np.fliplr([temp1])[0]
    x[17, 0:3] = temp2
    x[9:12, 2] = np.fliplr([temp3])[0]


def BackACW(x):  # action 12
    BackCW(x)
    BackCW(x)
    BackCW(x)

def make_move(x, move, reverse):
    # move number
    # reverse if 0 original move if 1 reverse of input move

    if reverse == 1:
        if move % 2 == 0:
            move = move - 1
        else:
            move = move + 1
    if move == 1:
        FrontCW(x)
        return "FrontCW"

    if move == 2:
        FrontACW(x)
        return "FrontACW"

    if move == 3:
        UpCW(x)
        return "UpCW"

    if move == 4:
        UpACW(x)
        return "UpACW"

    if move == 5:
        DownCW(x)
        return "DownCW"

    if move == 6:
        DownACW(x)
        return "DownACW"

    if move == 7:
        LeftCW(x)
        return "LeftCW"

    if move == 8:
        LeftACW(x)
        return "LeftACW"

    if move == 9:
        RightCW(x)
        return "RightCW"

    if move == 10:
        RightACW(x)
        return "RightACW"

    if move == 11:
        BackCW(x)
        return "BackCW"

    if move == 12:
        BackACW(x)
        return "BackACW"


