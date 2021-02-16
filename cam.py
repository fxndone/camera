from sys import executable
from os import get_terminal_size as gts, name, system

try:
    import numpy as np
except:
    try:
        system(executable + " -m pip install numpy")
    except:
        pass
try:
    from cv2 import cv2
except:
    try:
        system(executable + " -m pip install opencv-python")
    except:
        pass

from cv2 import cv2
import numpy as np

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
    return result


def grayToChar(gray):
    CHAR_LIST = ' .:-=+*#%@'
    num_chars = len(CHAR_LIST)
    return CHAR_LIST[
        min(
            int(gray * num_chars / 255),
            num_chars - 1
        )
    ]


if __name__ == "__main__":
    main()
