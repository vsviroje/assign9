import os

def main():
    file1=input("Enter File1 Name:")
    str= input("Enter String to match:")
    count=0
    if os.path.isfile(file1):
        f1=open(file1,'r')
        for line in f1:
            words=line.split(" ")
            for w in words:
                if w==str:
                    count=count+1

        print(str,"has frequency of ",count)

    else:
        print("any one or both provided file does not exists")


if __name__ == '__main__':
    main()
