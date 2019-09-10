import sys
def draw_museum(In):
    if In not in ["Vertical","Horizontal"]:   
        sys.exit()
    else:
        if In == "Horizontal":
            print(" ------ ")
            print("|Museum|")
            print(" ------ ")
        else:
            print(" --- ")
            print("| M |")
            print("| u |")
            print("| s |")
            print("| e |")
            print("| u |")
            print("| m |")
            print(" --- ")
    return 
