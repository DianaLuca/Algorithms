"""
At each step, examine the element just above the middle. 
If it belongs to the top group, swap it with the element just below the top. 
If it belongs in the bottom, swap it with the element just above the bottom. 
If it is in the middle, leave it. Update the appropriate index. 

Complexity is Θ(n) moves and examinations.[1]
"""


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


def dutch_national_flag(nums, mid):
    n = len(nums)
    lo, i, hi = 0, 0, n-1
    while lo <= hi:
        if nums[lo] < mid:
            swap(nums, i, lo)
            i += 1
            lo += 1
        elif nums[lo] > mid:
            swap(nums, lo, hi)
            hi -= 1
        else:
            lo += 1


def main():
    dnf = [0,2,1,0,2,0,0,0,0,1,1,1,2]
    dutch_national_flag(dnf, 1)
    print(dnf)


if __name__ == main():
    main()