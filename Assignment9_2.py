import os

def main():
    file=input("Enter File Name:")
    if os.path.isfile(file):
        toRead=open(file,'r')
        print(toRead.read())


if __name__ == '__main__':
    main()
