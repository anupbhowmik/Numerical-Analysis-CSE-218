from matplotlib import pyplot as plt
import numpy as np


def showGraphScatter(x, y):
    plt.scatter(x, y, color='red')
    plt.ylim(0, 0.4)
    plt.show()


def linearFunc(x, a_0, a_1):
    return a_0 + a_1 * x


def showGraph(lowerLim, upperLim, a_0, a_1, xarr, yarr):
    x = np.arange(lowerLim, upperLim, .1)
    y = []
    for i in range(x.size):
        y.append(linearFunc(x[i], a_0, a_1))
    plt.plot(x, y, color='blue')
    plt.ylim(0, 0.4)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(xarr, yarr, color='red')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='green')
    plt.axvline(x=0, color='green')
    plt.show()


def linear_regression(x, y, n):
    topLeft = 0
    x_sum = 0
    y_sum = 0
    bottomLeft = 0
    for i in range(n):
        topLeft += x[i] * y[i]
        x_sum += x[i]
        y_sum += y[i]
        bottomLeft += x[i] ** 2

    topLeft *= n
    bottomLeft *= n
    topRight = x_sum * y_sum
    bottomRight = x_sum ** 2

    a_1 = (topLeft - topRight) / (bottomLeft - bottomRight)
    a_0 = y_sum / n - a_1 * x_sum / n

    return a_0, a_1


def linear_regression_special(x, y, n):
    top = 0
    bottom = 0
    for i in range(1, n):
        top += x[i] * y[i]
        bottom += x[i] ** 2

    a = top / bottom
    return a


x = [0.698132, 0.959931, 1.134464, 1.570796, 1.919862]
y = [0.188224, 0.209138, 0.230052, 0.250965, 0.313707]

x1 = [0, 0.00183, 0.0036, 0.005324, 0.00702, 0.00867, 1.0244 / 100, 1.1774 / 100, 1.329 / 100, 1.479 / 100, 1.5 / 100,
      1.56 / 100]
y1 = [0, 306000000, 612000000, 917000000, 1223000000, 1529000000, 1835000000, 2140000000, 2446000000, 2752000000,
      2767000000, 2896000000]

# constants = linear_regression_special(x1, y1, 12)
constants = linear_regression(x, y, 5)
print(constants[0], constants[1])
# showGraphScatter(x, y)
# showGraph(x1, y1)
showGraph(0, 3, constants[0], constants[1], x, y)
