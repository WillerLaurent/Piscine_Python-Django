def read_file():
    file = open("numbers.txt", "r")
    str = file.read().split(',')
    for i in str:
        print(i)
    file.close()


if __name__ == '__main__':
    read_file()
