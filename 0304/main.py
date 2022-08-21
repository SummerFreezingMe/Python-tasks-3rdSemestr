import point as p


def max_square(points_list):
    triangle_square = 0
    suitable_triangle = []
    for i in points_list:
        for j in points_list:
            for k in points_list:
                if i.square_triangle(j, k) > triangle_square and i != j and i != k and j != k:
                    suitable_triangle.clear()
                    triangle_square = i.square_triangle(j, k)
                    suitable_triangle.extend([i, j, k])
    return suitable_triangle


def file_input(file_name):
    list = []
    f = open(file_name)
    points = f.readlines()
    for g in points:
        singular = g.split()
        list.append(p.Point(float(singular[0]), float(singular[1])))
    f.close()
    return list


if __name__ == '__main__':

    result = max_square(file_input("input5.txt"))
    for l in result:
        print(l.__str__())

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
