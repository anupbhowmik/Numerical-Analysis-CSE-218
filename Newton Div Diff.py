import numpy as np
from tabulate import tabulate as tb


# This is a general Interpolation program with relative approximate error
# Using n = 2 will work as Linear Interpolation

def divideDiff(x, y, n):
    for i in range(1, n):  # i starts from 1
        for j in range(0, n - i):
            y[j][i] = (y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j])


def printTable(y, n):
    for i in range(n):
        for j in range(n - i):
            print(y[i][j], end=' ')
        print('')


def findValue(x, y, n, x_val):
    value = y[0][0]  # y[0][0] = b1
    for i in range(1, n):
        productValue = 1
        for j in range(i):
            productValue *= (x_val - x[j])
        value += y[0][i] * productValue

    return value


def showRelativeErrorTable(x, y, n, x_val):
    table = [[]]
    prev = findValue(x, y, 2, x_val)
    table.append([1, prev, '--------------'])
    for i in range(3, n + 1):
        curr = findValue(x, y, i, x_val)

        error = abs(curr - prev) / curr * 100
        prev = curr
        table.append([i - 1, curr, error])

    print(tb(table, headers=['Order of polynomial', 'Current Value', 'Absolute Approximate Error%'], tablefmt='orgtbl'))


def print_b_values(y, n):
    for i in range(0, n):
        print('b', end='')
        print(i, '=', end='')
        print(y[0][i])


n = input('Enter n:')
n = int(n)
x = np.zeros(n)
y = np.zeros((n, n))
for i in range(n):
    print('Enter x', end='')
    print(i)
    x[i] = float(input())
    print('Enter y', end='')
    print(i)
    y[i][0] = float(input())

divideDiff(x, y, n)

x_input = float(input('Enter the value to evaluate function value:'))
print()
showRelativeErrorTable(x, y, n, x_input)
