from matplotlib import pyplot
import numpy as np
from tabulate import tabulate as tb


def func(x):
    return x / (1 - x) * ((2 * 3 / (2 + x))) ** 0.5 - 0.05


def showGraph():
    x = np.linspace(-5, 5, 1000)
    x = list(x)
    y = []

    for i in x:
        y.append(func(i))

    for i in range(len(y) - 1):
        if i > 0 and abs(y[i] - y[i - 1] > 10):
            x[i - 1] = np.nan
            x[i - 1] = np.nan

    print('Take a closer look at the graph and find the limits around the root.')
    pyplot.plot(x, y)
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.ylim(-10, 15)
    pyplot.title('x / (1 - x) * sqrt(2 * 3 / (2 + x)) - 0.05 = 0')
    pyplot.grid(True, which='both')
    pyplot.show()


def bisection(low, high, error, maxIteration=100):
    iteration = 1

    isFirstIteration = True
    midOld = 0.0
    e = 100  # initializing with 100% error

    while True:
        mid = (low + high) / 2 * 1.0
        if isFirstIteration == False:
            e = abs((mid - midOld) / mid) * 100

        midOld = mid;

        isFirstIteration = False

        if func(high) * func(mid) == 0:
            return mid
        if func(high) * func(mid) < 0:
            low = mid
        else:
            high = mid

        iteration += 1

        if e <= error:
            return mid
        if iteration > maxIteration and e > error:
            print('Max iteration reached but could not reach sufficiently close to the root.')
            print('Returning the root which has an error of:', e, '%')
            return mid


def bisectionTable(low, high, error, maxIteration=20):
    iteration = 1

    isFirstIteration = True
    midOld = 0.0

    table = [[]]
    while True:
        mid = (low + high) / 2 * 1.0

        if isFirstIteration == False:
            e = abs((mid - midOld) / mid) * 100
            table.append([iteration, mid, e])
        else:
            table = [[iteration, mid, 'N/A']]

        midOld = mid;

        isFirstIteration = False

        if func(high) * func(mid) < 0:
            low = mid
        else:
            high = mid

        iteration += 1

        if iteration > maxIteration:
            break

    print(tb(table, headers=['Iteration', 'value of root', '|error| %'], tablefmt='orgtbl'))


# ---------------------DEMONSTRATION BELOW-----------------------------#

showGraph()
x_l = input('Enter the lower limit:\n')
x_u = input('Enter the upper limit:\n')
approxError = input('Enter the approximation error:\n')
maxIteration = input('Enter the max iteration:\n')

x_u = float(x_u)
x_l = float(x_l)
approxError = float(approxError)
maxIteration = float(maxIteration)

# division by zero handling
if (x_l == 1):
    x_l = 1.00000000001
if (x_u == 1):
    x_u = 1.00000000001
if (x_l < -2):
    x_l = -1.9999999999999
if (x_u < -2):
    x_u = -1.9999999999999
# division by zero handling

while func(x_l) * func(x_u) > 0:
    showGraph()

    x_l = input('Enter the lower limit:\n')
    x_u = input('Enter the upper limit:\n')
    approxError = input('Enter the approximation error:\n')
    maxIteration = input('Enter the max iteration:\n')

    x_u = float(x_u)
    x_l = float(x_l)
    approxError = float(approxError)
    maxIteration = float(maxIteration)

root = bisection(x_l, x_u, approxError, maxIteration)
print('Approximate value of the root =', root)

bisectionTable(x_l, x_u, approxError, maxIteration)
