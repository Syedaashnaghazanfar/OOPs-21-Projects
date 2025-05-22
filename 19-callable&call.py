class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # set the factor during object creation
        print(f"Multiplier with factor {self.factor} created.")

    def __call__(self, value):
        result = self.factor * value
        print(f"Calling object: {self.factor} * {value} = {result}")
        return result

# Create an instance with a factor
double = Multiplier(2)
triple = Multiplier(3)

# Check if it's callable
print(callable(double))  # Output: True

# Use the object like a function!
print(double(5))  # Output: 10
print(triple(4))  # Output: 12
