"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples_three_five(x):
    kpsum = 0
    for i in range(1,x):
        if i % 3 == 0 or i % 5 == 0:
            kpsum += i
    return kpsum


def main():
    print(multiples_three_five(10))
    print(multiples_three_five(1000))

if __name__ == '__main__':
    main()

