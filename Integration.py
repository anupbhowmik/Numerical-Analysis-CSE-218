import math
from tabulate import tabulate as tb


def func(x):
    return 2000 * math.log((140000 / (140000 - 2100 * x)), math.e) - 9.8 * x


def trapezoidIntegration(lowerLim, upperLim, n):
    h = (upperLim - lowerLim) / n
    middleTerm = 0
    for i in range(1, n):
        middleTerm += 2 * func(lowerLim + i * h)
    result = h * (func(lowerLim) + middleTerm + func(upperLim)) / 2
    return result


def showTable_Trapezoidal(lowerLim, upperLim, n1, n2):
    table = [[]]
    prevValue = trapezoidIntegration(lowerLim, upperLim, n1)
    table.append([n1, prevValue, '---------------'])

    for i in range(n1 + 1, n2 + 1):
        currValue = trapezoidIntegration(lowerLim, upperLim, i)
        error = abs((currValue - prevValue) / currValue * 100.0)
        prevValue = currValue
        table.append([i, currValue, error])

    print(tb(table, headers=['n', 'Approximate Value', '|error| %'], tablefmt='orgtbl'))


def simpsonSingle(lowerLim, upperLim):
    h = (upperLim - lowerLim) / 2
    return h / 3 * (func(lowerLim) + 4 * func((lowerLim + upperLim) / 2) + func(upperLim))


def simpsonMultiple(lowerLim, upperLim, n):
    h = (upperLim - lowerLim) / (n)
    result = 0
    low = lowerLim
    for i in range(n):
        result += simpsonSingle(low, low + h)
        low = low + h
    return result


def showTable_Simpson(lowerLim, upperLim, n1, n2):
    table = [[]]
    prevValue = simpsonMultiple(lowerLim, upperLim, n1)
    table.append([n1, prevValue, '---------------'])

    for i in range(n1 + 1, n2 + 1):
        currValue = simpsonMultiple(lowerLim, upperLim, i)
        error = abs((currValue - prevValue) / currValue * 100.0)
        prevValue = currValue
        table.append([i, currValue, error])

    print(tb(table, headers=['n', 'Approximate Value', '|error| %'], tablefmt='orgtbl'))


n = int(input('Enter the number of sub-intervals (For Trapezoidal Rule):'))
result = trapezoidIntegration(8, 30, n)
print('Result from Trapezoidal Rule:', result)
showTable_Trapezoidal(8, 30, 1, 5)

n = int(input('Enter the number of sub-intervals (Simpson\'s Rule):'))
result = simpsonMultiple(8, 30, n)
print('Result from Simpson\'s Rule:', result)
showTable_Simpson(8, 30, 1, 5)

# result of the integration = 11061.335568081007
