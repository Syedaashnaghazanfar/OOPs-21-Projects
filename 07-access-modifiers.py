class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("John", 50000, "123-45-6789")
print(emp.name)         # Public - works
print(emp._salary)      # Protected - works but not recommended
# print(emp.__ssn)      # Private - Error
print(emp._Employee__ssn)  # Name mangling - works but discouraged

# The __ssn attribute is private and cannot be accessed directly from outside the class.
# However, it can be accessed using name mangling (prefixing the attribute with _ClassName).
# This is not recommended as it breaks encapsulation.
# The _salary attribute is protected and can be accessed, but it is not recommended to do so from outside the class.
