from sys import executable
from threading import Event, Thread
from os import get_terminal_size as gts, name, system
from pickle import dump

toDl = []

try:
    import numpy as np
except:
    toDl.append("numpy")
try:
    from cv2 import cv2
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

allImgs = []

def waitForEnter():
    input()
    e.set()

e = Event()

def dp(obj):
    for i in range(1, 100):
        try:
            open(f"video{str(i)}.video", "rb").close()
        except:
            fileName = f"video{str(i)}.video"
            break
    try:
        dump(obj, open(fileName, "wb+"))
    except:
        print("To many videos !")
        dump(obj, open("I Hope it is the last.video", "wb+"))

if name == "nt":
    def cls():
        system("cls")
else:
    def cls():
        system("clear")

cls()

Thread(target=waitForEnter, daemon=True).start()

def main():
    vc = cv2.VideoCapture(0)

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        try:
            rval, frame = vc.read()
            h, w = gts()
            img = toASCII(frame, h, w)
            allImgs.append(img)
            print(img)
            key = cv2.waitKey(40)
            if key == 27 or e.is_set():
                break
        except:
            break
    dp(allImgs)


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
