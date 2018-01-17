from BubbleSort import bubble_sort
from MergeSort import merge_sort


def test():
    N = 1000
    arr = list(range(N, 0, -1))
    assert bubble_sort(arr) == merge_sort(arr)


if __name__ == '__main__':
    test()