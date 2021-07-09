class Employee:
    'documentation here'
    empCount = 0

    # this is like static var
    # nothing is private in python
    # self parameter is absolutely necessary for function definition

    def __init__(self):
        print('Default called')
        Employee.empCount += 1

    def __init__(self, name, salary):
        '__funcName__ is a built in library func, we are overriding it'
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        # empCount is like a static var, so, we have to call it using the class name

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayDetais(self):
        print('Name:', self.name, 'Salary:', self.salary)
        return self.name, self.salary


emp1 = Employee('Anup', 1000)
emp2 = Employee('Anup', 1000)
emp2.name = "Bhai"
emp2.salary = "2000"
em = Employee
# emp1.displayCount()
print(Employee.empCount)
emp2.displayDetais()
em = emp1.displayDetais()
print(em)

# __new__ diye python actually object create kore
# __new__ paile python automatically __init__ call kore
