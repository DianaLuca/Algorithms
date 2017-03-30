def main():
    list = [1, 10, 30, 15]
    x = 15
    index = linear_search(list, x)

    if index == -1:
        print("Element {} is not in list".format(x))
    else:
        print("{} is present at index {}".format(x, linear_search(list, x)))


def linear_search(list, x):
    n = len(list)
    for i in range(0,n):
        if list[i] == x:
            return i
    return -1

if __name__ == "__main__": main()