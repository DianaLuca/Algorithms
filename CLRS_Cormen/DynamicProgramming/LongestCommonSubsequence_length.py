"""
Procedure LCS-LENGTH takes two sequences X D hx1; x2; : : : ; xmi and Y Dhy1;y2;:::;yni as inputs. 
It stores the cŒi;j values in a table cŒ0::m;0::n , and it computes the entries in row-major order. 
(That is, the procedure fills in the first row of c from left to right, then the second row, and so on.) 
The procedure also maintains the table bŒ1 : : m; 1 : : n  to help us construct an optimal solution. 
Intuitively, bŒi;j  points to the table entry corresponding to the optimal subproblem solution chosen when computing cŒi; j  . 
The procedure returns the b and c tables; cŒm; n  contains the length of an LCS of X and Y .


X D hA;B;C;B;D;A;Bi and 
Y D hB;D;C;A;B;Ai. 
The running time of the procedure is ‚.mn/, since each table entry takes ‚.1/ time to compute.

"""


def LCS_lengths(X, Y):
    m = len(X)
    n = len(Y)

    B, C = [[0 for _ in range(n)] for _ in range(m)], [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                C[i][j] = 1 + C[i-1][j-1]
                B[i][j] = "\\"
            elif C[i-1][j] >= C[i][j-1]:
                C[i][j] = C[i-1][j]
                B[i][j] = "|"
            else:
                C[i][j] = C[i][j-1]
                B[i][j] = "<-"

    print("B = ")
    for i in range(m):
        for j in range(n):
            print(B[i][j], end="  ")
        print()

    print("C = ")
    for i in range(m+1):
        for j in range(n+1):
            print(C[i][j], end=",")
        print()


X = ["a", "b", "c", "b", "d", "a", "b"]
Y = ["b", "d", "c", "a", "b", "a"]
LCS_lengths(X, Y)