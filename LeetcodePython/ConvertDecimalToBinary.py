"""
transform a decimal to binary
"""

def decToBin(n):
    res = []
    while n > 0:
        mod = n % 2
        res.append(mod)
        n = int((n-mod)/2)
    res.append(0)
    bin = ''

    for i in res[::-1]:
        bin = bin + str(i)
    return bin

n = 12
print(decToBin(n))