import sys



def print_hi(list_of_integer):
    print(list_of_integer)
    negative = 0
    for i in range(len(list_of_integer)):
        if list_of_integer[i] < 0:
            list_of_integer.insert(negative, list_of_integer.pop(i))
            negative += 1
    print(list_of_integer)
    print(sys.executable)


if __name__ == '__main__':
    l = [-1, 3, 7, -5, -8, 2, 77, 9, 0, -4, 3]
    print_hi(l)
