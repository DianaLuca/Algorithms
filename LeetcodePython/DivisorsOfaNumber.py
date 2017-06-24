import math


def divisors(n):
    result = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}  # reunion
    return result


print(divisors(144))
