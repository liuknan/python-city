import math


def draw_museum(direction, length):
    museum = ["M", "u", "s", "e", "u", "m"]
    if direction not in ["Vertical", "Horizontal"]:
        raise ValueError
    if length <= 0:
        raise ValueError
    else:
        length = math.ceil(length)
        if direction == "Horizontal":
            print(" ", end="")
            for _ in range(length):
                print("-", end="")
            print(" ")
            print("|", end="")
            if length > 6:
                start = length // 2 - 3
                end = start + 5
                num = 0
                for i in range(length):
                    if start <= i <= end:
                        print(museum[num], end="")
                        num += 1
                    else:
                        print(" ", end="")
            else:
                for i in range(length):
                    print(museum[i], end="")
            print("|")
            print(" ", end="")
            for _ in range(length):
                print("-", end="")
            print(" ")
        else:
            if length > 6:
                start = length // 2 - 3
                end = start + 5
                num = 0
                print(" --- ")
                for i in range(length):
                    if start <= i <= end:
                        print(" |", end="")
                        print(museum[num], end="")
                        num += 1
                        print("|")
                    else:
                        print(" | |")
                print(" --- ")
            else:
                print(" --- ")
                for i in range(length):
                    print("|"+museum[i]+"|")
                print(" --- ")
    return

