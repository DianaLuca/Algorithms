# 1. Sort points according to their x-coordinates.
# 2. Split the set of points into two equal-sized subsets by a vertical line x=xmid.
# 3. Solve the problem recursively in the left and right subsets.
# This yields the left-side and right-side minimum distances dLmin and dRmin, respectively.
# 4. Find the minimal distance dLRmin among the set of pairs of points in which one point
# lies on the left of the dividing vertical and the other point lies to the right.
# 5. The final answer is the minimum among dLmin, dRmin, and dLRmin.
#
# Given 2 list of points with x and respective y coordinates,
# produce a minimal distance between a pair of 2 points.

import math
import random
import sys

# ============ O(NlogN) Solution ================


def solution(x, y):
    a = list(zip(x, y))  # this produces list of tuples
    ax = sorted(a, key=lambda x: x[0])  # presorting x-wise
    ay = sorted(a, key=lambda x: x[1])
    cnt = 0
    p1, p2, mi, counter = closest_pair(ax, ay, cnt)  # Recursive Divide & Conquer solution
    # print('Counter =', counter)
    return mi


def closest_pair(ax, ay, cnt):
    ln_ax = len(ax)
    if ln_ax <= 1:
        return ax, None, cnt + 1

    if ln_ax == 2:
        return ax[0], ax[1], dist(ax[0], ax[1]), cnt + 1

    mindist = sys.maxsize
    if ln_ax == 3:
        for i in range(2):
            for j in range(i+1, ln_ax):
                cnt += 1
                if dist(ax[i], ax[j]) < mindist:
                    pcrr, qcrr, mindist = ax[i], ax[j], dist(ax[i], ax[j])

        return pcrr, qcrr, mindist, cnt

    # if ln_ax <= 3:
    #     return closestPairBrute(ax)

    mid = ln_ax // 2
    Qx = ax[:mid]
    Rx = ax[mid:]

    # Determine midpoint on x-axis

    midpoint = ax[mid][0]

    Qy = list()
    Ry = list()
    for x in ay:
        if x[0] <= midpoint:
            Qy.append(x)
        else:
            Ry.append(x)

    # Call recursively both arrays after split

    (p1, q1, mi1, cnt1) = closest_pair(Qx, Qy, cnt)
    (p2, q2, mi2, cnt2) = closest_pair(Rx, Ry, cnt)

    # Determine smaller distance between points of 2 arrays

    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    # Call function to account for points on the boundary

    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)

    # Determine smallest distance for the array

    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3


# ========== Call function to account for points on the boundary ================


def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)
    midpoint_x = p_x[ln_x // 2][0]  # select midpoint on x-sorted array

    # Create a subarray of points not further than delta
    # from midpoint on x-sorted array

    s_y = [x for x in p_y if midpoint_x - delta <= x[0] <= midpoint_x + delta]

    best = delta
    ln_y = len(s_y) # length of subarray =roughly= 2*delta

    for i in range(ln_y - 1):
        for j in range(i+1, min(i+7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst

    return best_pair[0], best_pair[1], best



# ====================== BruteForce: O(N**2) ==============================

def closestPairBrute(ax):
    ln_ax = len(ax)
    counter = 0

    if ln_ax <= 1:
        return ax, None, 0, counter

    p1 = ax[0]
    p2 = ax[1]
    mi = dist(p1, p2)

    for i in range(ln_ax - 1):
        for j in range(i+1, ln_ax):
            counter += 1
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:
                    mi = d
                    p1, p2 = ax[i], ax[j]

    # print("Counter BruteForce: ", counter)
    return p1, p2, mi, counter


# =========== EUCLIDIAN DISTANCE BTW 2 POINTS IN PLAN =================


def dist(p1,p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# print(dist([1,1], [2,2]))
# print(1 * math.sqrt(2))
# print(2 ** 3)


# ================ TEST CASE =====================


def test_case(length : int = 10000):
    lst1 = [random.randint(-10**9, 10**9) for i in range(length)]
    lst2 = [random.randint(-10**9, 10**9) for i in range(length)]
    return lst1, lst2


# =========== DRAFT +++++++++++++
def test_counter(param):
    counter = 0
    for i in range(param -1):
        for j in range(i+1, param):
            counter += 1

    print("Number of iterations for param = {}, is iter_nr = {} ".format(param, counter))


for i in range(1):
    (lst1, lst2) = test_case(4)
    a = list(zip(lst1, lst2))  # create a list of tuples [(.. , ..) .. , .. (.. , ..)
    ax = sorted(a, key=lambda x: x[0])  # presorting x-wise
    (p, q, brutedis, counter) = closestPairBrute(ax)
    print('\np = {}, q = {}, distance_bruteForce = {}, number_of_iterations = {}'.format(p, q, brutedis, counter))

    # solution = solution(lst1, lst2)
    # print('distance_NlogN ====== {}'.format(solution))

    # assert (brutedis == solution)
#
# test_counter(6)