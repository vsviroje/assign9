import os

def main():
    file1=input("Enter File1 Name:")
    file2= input("Enter File2 Name:")
    if os.path.isfile(file1) and os.path.isfile(file2):
        f1=open(file1,'r')
        f2=open(file2,'r')
        rf1=f1.readlines()
        rf2=f2.readlines()
        if rf1==rf2:
            print("both file are same")
        else:
            print("not same")
    else:
        print("any one or both provided file does not exists")


if __name__ == '__main__':
    main()
