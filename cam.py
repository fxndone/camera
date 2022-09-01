from sys import executable
from os import get_terminal_size as gts, name, system

toDl = []

try:
    import numpy as np
except:
    toDl.append("numpy")
try:
    import cv2
except:
    toDl.append("opencv-python")

if toDl != []:
    print("/!\\Need to install modules/!\\")
    for ele in toDl:
        print(f"-{ele}")
    chx = str(input("Install ? (Y/N) : "))
    while chx.lower() != "y" and chx.lower() != "n":
        chx = str(input("Install ? (Y/N) : "))
    if chx.lower() == "n":
        print("Modules required !!")
        print("Exiting...")
        exit()
    else:
        for ele in toDl:
            try:
                system(executable + f" -m pip install {ele}")
            except:
                pass
        try:
            from cv2 import cv2
            import numpy as np
        except:
            print("/!\\Chec your pip installer !!/!\\")
            print("Exiting...")
            exit()

if name == "nt":
    def cls():
        system("cls")
else:
    def cls():
        system("clear")

cls()

def main():
    vc = cv2.VideoCapture(0)

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        rval, frame = vc.read()
        h, w = gts()
        print(toASCII(frame, h, w))
        key = cv2.waitKey(50)
        if key == 27:
            break


def rev(string):
    return '\n'.join([x[::-1] for x in string.split('\n')])


def toASCII(frame, cols=120, rows=35):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = frame.shape
    cell_width = width / cols
    cell_height = height / rows
    if cols > width or rows > height:
        raise ValueError('Too many cols or rows.')
    result = ""
    for i in range(rows):
        for j in range(cols):
            gray = np.mean(
                frame[int(i * cell_height):min(int((i + 1) * cell_height), height),
                int(j * cell_width):min(int((j + 1) * cell_width), width)]
            )
            result += grayToChar(gray)
        result += '\n'
    return rev(result)


def grayToChar(gray):
    CHAR_LIST = ' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$' # ' .:-=+*|#%@'
    num_chars = len(CHAR_LIST)
    return CHAR_LIST[
        min(
            int(gray * num_chars / 255),
            num_chars - 1
        )
    ]


if __name__ == "__main__":
    main()
