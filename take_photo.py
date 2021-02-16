from sys import executable
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
                system(executable + " -m pip install opencv-python")
            except:
                pass
        try:
            from cv2 import cv2
            import numpy as np
        except:
            print("/!\\Chec your pip installer !!/!\\")
            print("Exiting...")
            exit()
    
    
def save(data):
    for i in range(1, 100):
        try:
            open(f"img{str(i)}.image", "r").close()
        except:
            imgName = f"img{str(i)}.image"
            break
    try:
        dump(data, open(imgName, "wb+"))
    except:
        print("To many files !")
        dump(data, open("I Hope it is the last.image", "wb+"))


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

    if not rval:
        print("Not working !\nYour camera isn't good !")
        exit()
    h, w = gts()
    save(toASCII(frame, h, w))


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
