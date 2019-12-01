import os

def main():
    file=input("Enter File/Folder Name:")
    if os.path.exists(file):
        print("It exist")
    else:
        print("It does not exist")

if __name__ == '__main__':
    main()

