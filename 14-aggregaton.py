class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee


    def display(self):
        print(f"Employee Name: {self.employee.name}")
# Create an instance of Employee
employee1 = Employee("John Doe")
# Create an instance of Department with the employee instance
department1 = Department(employee1)

# Display the employee name through the department instance
department1.display()  # Output: Employee Name: John Doe
# The Department class aggregates the Employee class by holding a reference to an Employee instance.
# This is an example of aggregation, where one class (Department


# ) contains a reference to another class (Employee) but does not own it.
# Aggregation is a design principle where one class contains a reference to another class, but the contained class can exist independently.