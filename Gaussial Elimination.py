import numpy as np
from pip._vendor.distlib.compat import raw_input


def gaussianElimination(A, B, d):
    # FORWARD ELIMINATION
    n = B.size

    i = 0
    while i < n:
        j = i + 1
        while j < n:
            # RATIO = R2/R1
            r = A[j][i] / A[i][i]

            k = 0
            while k < n:
                #   (R2 = R2 - R1 * r)
                A[j][k] -= r * A[i][k]

                k += 1

            B[j] -= r * B[i]
            if d:
                print('Coefficient Matrix:')
                print(A)
                print('Constant Matrix:')
                print(B)

            j += 1
            print()
        i += 1

    # BACK SUBSTITUTION
    solution = np.zeros(n)
    # CALCULATING THE VALUE OF THE LAST VARIABLE
    solution[n - 1] = B[n - 1] / A[n - 1][n - 1]

    # FINDING THE REST OF THE SOLUTIONS USING THE PREVIOUS SOLUTIONS
    i = n - 2
    while i >= 0:
        solution[i] = B[i]
        j = i + 1
        while j < n:
            solution[i] = solution[i] - A[i][j] * solution[j]
            j += 1
        solution[i] /= A[i][i]
        i -= 1

    return solution


# -------------------------DEMONSTRATION---------------------------------#

numOfUnknowns = input('Enter the number of unknown variables: ')
numOfUnknowns = int(numOfUnknowns)
matA = np.zeros((numOfUnknowns, numOfUnknowns))
matB = np.zeros(numOfUnknowns)

print('Enter the coefficients: (in row major order)')
i = 0
while i < numOfUnknowns:
    matA[i] = [float(x) for x in raw_input().split()]
    i += 1

print('Enter the constants:')

i = 0
while i < numOfUnknowns:
    matB[i] = float(input())
    i += 1

solution = gaussianElimination(matA, matB, True)

print('\nSolution Vector:')
i = 0
while i < numOfUnknowns:
    print(f"{solution[i]:.4f}")
    i += 1
