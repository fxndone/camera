from os import name, system
from pickle import load

def dump(filename):
    obj = load(open(filename, "rb"))
    print("\n")
    print(obj)

if name == "nt":
    def cls():
        system("cls")
else:
    def cls():
        system("clear")

cls()

def main():
    for i in range(1, 100):
        try:
            dump(f"img{str(i)}.image")
        except:
            pass
        else:
            exit()
    file = str(input("Please enter file name : "))
    dump(file)

if __name__ == "__main__":
    main()
