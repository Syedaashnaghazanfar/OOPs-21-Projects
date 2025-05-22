# Step 1: Define the class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # Dynamically add greet() method to the class
    return cls

# Step 2: Apply decorator to a class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person {self.name} created.")
    # The greet method is added dynamically by the decorator

# Step 3: Test it
p = Person("Ashna")
print(p.greet())  # Output: Hello from Decorator!
