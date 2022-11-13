import math
import sys


def enum(arr):
    # считывание и сортировка массива чисел
    arr.sort()

    if len(arr) % 2 != 0:
        median_index = math.floor(len(arr) / 2)
    else:
        median_index = len(arr) // 2

    median = arr[median_index]

    count = 0
    for i, item in enumerate(arr):
        while item != median:
            if item < median:
                item += 1
                count += 1
            elif item > median:
                item -= 1
                count += 1
            else:
                arr[i] = item
    print(count)


def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file1:
        a = list(map(int, file1.readlines()))
        enum(a)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        read_from_file(sys.argv[1])
    else:
        sys.exit(1)