def column_exclusion(arr):
    arr = trans(arr)
    new_array = []
    for i in arr:
        if i not in new_array:
            new_array.append(i)
    return trans(new_array)


def trans(arr):
    rows = len(arr)
    cols = len(arr[0])
    return [[arr[i][j] for i in range(rows)] for j in range(cols)]


def print_array(arr):
    for i in arr:
        print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array = [[1, 2, 3, 2, 2, 2, 100, 0, 0],
             [4, 5, 6, 5, 2, 5, 100, 7, 7],
             [7, 8, 9, 8, 8, 1008, 5, 2, 2]]
    print_array(array)
    print("-" * 30)
    print_array(column_exclusion(array))
