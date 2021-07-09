import math
import matplotlib.pyplot as plt
import numpy as np


def showGraphScatter(x, y):
    plt.scatter(x, y)
    plt.show()


def expFunc(x, a_0, a_1):
    return a_0 * math.e ** (a_1 * x)


def showGraph(lowerLim, upperLim, a_0, a_1, xarr, yarr):
    x = np.arange(lowerLim, upperLim, .1)
    y = []
    for i in range(x.size):
        y.append(expFunc(x[i], a_0, a_1))
    plt.plot(x, y, color='blue')
    plt.ylim(0, 1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(xarr, yarr, color='red')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='green')
    plt.axvline(x=0, color='green')
    plt.show()


def exponentialRegression(x, y, n):
    # mapped to ln
    topLeft = 0
    x_sum = 0
    z_sum = 0
    bottomLeft = 0
    for i in range(n):
        topLeft += x[i] * math.log(y[i])
        x_sum += x[i]
        z_sum += math.log(y[i])
        bottomLeft += x[i] ** 2

    topLeft *= n
    bottomLeft *= n
    topRight = x_sum * z_sum
    bottomRight = x_sum ** 2

    a_1 = (topLeft - topRight) / (bottomLeft - bottomRight)
    a_0 = z_sum / n - a_1 * x_sum / n

    return math.e ** a_0, a_1


x = [0, 1, 3, 5, 7, 9]
y = [1, 0.891, 0.708, 0.562, 0.447, 0.355]
constants = exponentialRegression(x, y, 6)
print(constants[0], constants[1])
showGraph(0, 30, constants[0], constants[1], x, y)
