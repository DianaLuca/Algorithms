def convertBaseTwo(x, b):
    if b == 2 and x <= 1:
        return str(x)
    elif b == 10 and x <= 9:
        return str(x)
    return convertBaseTwo(x//b, b) + str(x%b)

x, b2 = 127, 2
print(convertBaseTwo(x, b2))

y, b10 = 128, 10
print(convertBaseTwo(y, b10))


