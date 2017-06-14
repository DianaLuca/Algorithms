# Given a positive integer, output its complement number.
# The complement strategy is to flip the bits of its binary representation.
#
# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.

def findComplement(nr):
    mask = 1 << (len(bin(nr)) - 2)  # 'ob...'
    return nr ^ (mask - 1)


def findComplementNonInterestingSolution(num):
    """
    :type num: int
    :rtype: int
    """

    # Wikipedia:
    # mask = 2**31
    # return -(num & mask) + (num & ~mask)

    binNum = bin(num)
    res = ''
    for i in range(2,len(binNum)):
        if binNum[i] == '0':
            res += '1'
        else:
            res += '0'
    return int(res, 2)


print(findComplement(100))