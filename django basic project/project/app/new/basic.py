class Employee:
    employeecount=0
    employeesalary=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        Employee.employeesalary += self.salary
        Employee.employeecount += 1

    def sumofsalary(self):


        print(Employee.employeesalary)
        print(Employee.employeecount)

employees = [Employee("Adira",5000), Employee("Manisha",12000)]
Employee.sumofsalary()