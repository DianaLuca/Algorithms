"""
Given an array of integers where each element represents the max number of steps that can be made forward from that element. 
Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). 
If an element is 0, then cannot move through that element.

Example:

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 ->9)
"""

""" In this method we construct an array "jumps[]" from left to right, such that jumps[i] indicates
the minimum number of jumps needed to reach arr[i] from arr[0].
Finally we return jumps[n-1]."""

def minJumpsLeftToRight(arr, n):
    jumps = [0 for _ in range(n)]

    if n == 0 or arr[0] == 0:
        return float('inf')

    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[n-1]

""" In this method we build jumps[] array from right to left such that jumps[i] represents
the minimum number of jumps needed to reach arr[n-1] from arr[i]
"""
def minJumpsRightToLeft(arr, n):
    pass


def main():
    arr = [1, 13, 6, 1, 0, 9]
    n = len(arr)
    print(minJumpsLeftToRight(arr, n))

if __name__ == '__main__':
    main()