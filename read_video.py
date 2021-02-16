from sys import executable
from os import get_terminal_size as gts, name, system
from pickle import load
from time import sleep

if name == "nt":
    def cls():
        system("cls")
else:
    def cls():
        system("clear")

cls()

def dump(filename):
    obj = load(open(filename, "rb"))
    for ele in obj:
        print(ele)
        print('\n')
        sleep(0.1)

def main():
    for i in range(1, 100):
        try:
            dump(f"video{str(i)}.video")
        except KeyboardInterrupt:
            exit()
        except:
            pass
        else:
            exit()
    file = str(input("Please enter file name : "))
    dump(file)

if __name__ == "__main__":
    main()
