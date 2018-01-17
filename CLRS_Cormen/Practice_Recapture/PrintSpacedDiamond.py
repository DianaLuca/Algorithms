"""
N = 2:
_*_
*_*
_*_

N = 3:
__*__
_*_*_
*_*_*
_*_*_
__*__

"""


def print_spaced_diamond(n):
    width = 2 * n - 1
    pattern_len = list(range(1, width + 2, 2)) + list(range(width - 2, -1, -2))

    for pat in pattern_len:
        spaces = (width - pat) // 2
        pattern = ''
        for i in range(pat):
            if i % 2 == 0:
                pattern += "*"
            else:
                pattern += " "
        print(' ' * spaces + pattern)


def main():
    for N in range(5):
        print("N =", N)
        print_spaced_diamond(N)
        print()

if __name__ == main():
    main()