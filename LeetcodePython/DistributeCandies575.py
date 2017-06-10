# Given an integer array with even length, where different numbers in this array represent different kinds of candies.
# Each number means one candy of the corresponding kind.
# You need to distribute these candies equally in number to brother and sister.
# Return the maximum number of kinds of candies the sister could gain.

# from collections import Counter


def distributeCandies(candies):
    n = len(candies)
    s = set(candies)
    unique = len(s)

    if unique < n//2:
        return unique
    else:
        return n//2