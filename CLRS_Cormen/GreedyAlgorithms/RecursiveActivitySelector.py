# Greedy - Iterative - Activity - Selector(A, s, f):
#
# Sort A by finish times stored in f'
#
# S = {A[1]}
# k = 1
#
# n = A.length
#
# for i = 2 to n:
#     if s[i] ≥ f[k]:
#         S = S U {A[i]}
#         k = i
#
# return S


def activity_selector(A):
    # A = [(3,4), (0,6), (1,2), (5,9), (5,7), (8,9)]
    A.sort(key=lambda x: x[1])  # sorting a list of tuples by the second value
    start, finish,  = list(), list()
    for t in A:
        start.append(t[0])
        finish.append(t[1])

    n, k, res = len(A), 0, list()
    for i in range(1,n):
        if start[i] >= finish[k]:
            res.append(A[i])
            k = i
    return res


# Driver program to test above function
A = [(3,4), (0,6), (1,2), (5,9), (5,7), (8,9)]
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]

actions = activity_selector(A)
print(actions)

