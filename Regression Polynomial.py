import numpy as np
from matplotlib import pyplot as plt


def showGraphScatter(x, y):
    plt.scatter(x, y, color='red')
    plt.show()


def polynomialFunc(x, constants):
    funcVal = constants[0]
    constants = np.array(constants)
    for i in range(1, constants.size):
        funcVal += constants[i] * x
        x *= x

    return funcVal


def showGraph(lowerLim, upperLim, constants, xarr, yarr):
    x = np.arange(lowerLim, upperLim, .1)
    y = []
    for i in range(x.size):
        y.append(polynomialFunc(x[i], constants))
    plt.plot(x, y, color='blue')
    # plt.ylim(0, 0.4)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(xarr, yarr, color='red')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='green')
    plt.axvline(x=0, color='green')
    plt.show()


def gaussianElimination(A, B, d=0):
    # FORWARD ELIMINATION
    i = 0
    n = B.size
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


def polynomialRegression(x, y, numOfDataPoints, degree):
    # degree = 1 for linear regression
    x = np.array(x)
    y = np.array(y)
    x_exp_sums = np.zeros(2 * degree + 1)
    x_exp_y_sums = np.zeros(2 * degree + 1)
    x_exp_sums[0] = numOfDataPoints
    x_exp_y_sums[0] = sum(y)

    power_x = np.ones(len(x))
    for i in range(1, 2 * degree + 1):
        power_x = power_x * x
        for j in range(numOfDataPoints):
            x_exp_sums[i] += power_x[j]
            x_exp_y_sums[i] += y[j] * power_x[j]

    matA = np.zeros((degree + 1, degree + 1))
    matB = np.zeros(degree + 1)

    for i in range(degree + 1):
        matB[i] = x_exp_y_sums[i]
        for j in range(degree + 1):
            matA[i][j] = x_exp_sums[i + j]

    return gaussianElimination(matA, matB)


x = [80, 40, -40, -120, -200, -280, -340]
y = [6.47e-6, 6.24e-6, 5.72e-6, 5.09e-6, 4.30e-6, 3.33e-6, 2.45e-6]
# showGraphScatter(x, y)
constants = polynomialRegression(x, y, 7, 4)
showGraph(-400, 200, constants, x, y)
print('result', constants)
