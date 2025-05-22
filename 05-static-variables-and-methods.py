class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
# Example usage
result1 = MathUtils.add(5, 3)
result2 = MathUtils.subtract(10, 4)
result3 = MathUtils.multiply(2, 6)
result4 = MathUtils.divide(8, 2)
print(f"Addition: {result1}")        # Output: Addition: 8
print(f"Subtraction: {result2}")     # Output: Subtraction: 6
print(f"Multiplication: {result3}")  # Output: Multiplication: 12
print(f"Division: {result4}")        # Output: Division: 4.0
# The static methods add, subtract, multiply, and divide are defined within the MathUtils class.
# They can be called directly on the class without creating an instance.
# Static methods are used for utility functions that don't require access to instance or class variables.