def linear_search(l, x):
    n = len(l)
    for i in range(0, n):
        if l[i] == x:
            return i
    return -1

def main():
    l = [1, 10, 30, 15]
    x = 15
    index = linear_search(l, x)

    if index == -1:
        print("Element {} is not in list".format(x))
    else:
        print("{} is present at index {}".format(x, linear_search(l, x)))

if __name__ == "__main__":
    main()