from matplotlib import pyplot
import numpy as np
from tabulate import tabulate as tb


def func(x):
    return x ** 3 + 2 * x - 2


def derivativeFunc(x):
    return 3 * x ** 2 + 2


def showGraph():
    x = np.linspace(-5, 5, 1000)
    x = list(x)
    y = []
    for i in x:
        y.append(func(i))

    pyplot.plot(x, y)
    pyplot.xlabel('X')
    pyplot.ylabel('Y')
    pyplot.grid(True, which='both')
    pyplot.ylim(-5, 5)
    pyplot.show()


def newtonRaphson(a, e, max):
    root = a - func(a) / derivativeFunc(a)
    error = 100
    i = 0;
    while i < max:
        if error <= e:
            return root
        currRoot = root - func(root) / derivativeFunc(root)
        error = abs(currRoot - root) / currRoot * 100
        root = currRoot

        i += 1

    return currRoot


def showTable(a, e, max):
    root = a - func(a) / derivativeFunc(a)
    error = 100
    i = 0;
    table = [[]]
    while i <= max:
        currRoot = root - func(root) / derivativeFunc(root)
        error = abs(currRoot - root) / currRoot * 100
        root = currRoot


        table.append([i, root, error])
        i += 1

    print(tb(table, headers=['Iteration', 'value of root', '|error| %'], tablefmt='orgtbl'))


showGraph()

root = newtonRaphson(5, 0.5, 100)
print('Value of root:', root)
print()
showTable(5, 0.5, 20)
