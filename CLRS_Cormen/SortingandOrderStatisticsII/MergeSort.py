"""
O(NlogN) time complexity
O(N) stack memory complexity
"""


def merge(a, b):
    c = list()
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:  # len(a) not 0
        c += a
    return c


def merge_sort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) <= 1:
        return x
    else:
        middle = len(x)//2
        a = merge_sort(x[:middle])
        b = merge_sort(x[middle:])
        return merge(a, b)


def main():
    arr = [4, 1, 7, 4, 2, 3, 9]
    res = merge_sort(arr)
    print(res)

if __name__ == '__main__':
    main()
