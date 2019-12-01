import os

def main():
    file=input("Enter File Name:")
    if os.path.isfile(file):
        toRead=open(file,'r')
        toWrite=open("Demo2.txt",'w')
        data=toRead.read()
        toWrite.writelines(data)


if __name__ == '__main__':
    main()
