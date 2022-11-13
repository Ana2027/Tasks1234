import sys


def find_way(n, m):
    i = 1
    while True:
        print(i, end='')
        i = 1 + (i + m - 2) % n
        if i == 1:
            break


if __name__ == "__main__":
    if len(sys.argv) == 3:
        find_way(int(sys.argv[1]), int(sys.argv[2]))
    else:
        sys.exit(1)
