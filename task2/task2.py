import sys
import math


def way(cx, cy, rad, points):
    for point in points:
        res = math.sqrt(((float(point[0]) - cx) ** 2) + (float(point[1]) - cy) ** 2)
        if res > rad:
            print(2)
        elif res == rad:
            print(0)
        else:
            print(1)


def is_in_circle(circle_file, dot_file):
    with open(circle_file, 'r', encoding='utf-8') as file_1, open(dot_file, 'r', encoding='utf-8') as file_2:
        circle = list(map(lambda it: it.split(), file_1.readlines()))
        center_x, center_y = float(circle[0][0]), float(circle[0][1])
        radius = float(circle[1][0])
        points = list(map(lambda it: it.split(), file_2.readlines()))
        if not 1 <= len(points) <= 100:
            raise ValueError('Points quantity must be in [1, 100]')
        way(center_x, center_y, radius, points)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        is_in_circle(sys.argv[1], sys.argv[2])
    else:
        sys.exit(1)


