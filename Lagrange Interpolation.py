from tabulate import tabulate as tb

def lagrangeInterpolation(x, y, n, value):
    result = 0
    for i in range(n):
        currTerm = y[i]  # hiding x[i]
        for j in range(n):
            if j != i:
                currTerm *= (value - x[j]) / (x[i] - x[j])  # now using the previously hidden x[i]
        result += currTerm
    return result

def showRelativeErrorTable(x, y, n, value):
    table = [[]]
    prev = lagrangeInterpolation(x, y, 2, value)
    table.append([1, prev, '--------------'])
    for i in range(3, n + 1):
        curr = lagrangeInterpolation(x, y, i, value)

        error = abs(curr - prev) / curr * 100
        prev = curr
        table.append([i - 1, curr, error])

    print(tb(table, headers=['Order of polynomial', 'Current Value', 'Absolute Approximate Error%'], tablefmt='orgtbl'))


x = []
y = []
n = int(input('Enter number of interpolants:'))
for i in range(n):
    x.append(float(input()))
    y.append(float(input()))

value = float(input('Enter the value to evaluate function value:'))
result = lagrangeInterpolation(x, y, n, value)
print(result)
showRelativeErrorTable(x, y, n, value)
