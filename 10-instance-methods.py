class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")
        print(f"{self.name} is a {self.breed}.")

# Create an instance of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()  # Output: Buddy is barking!
# The bark method is an instance method that operates on the instance of the Dog class.
# Instance methods are defined with the first parameter as self, which refers to the instance itself.
# They can access instance variables and perform actions specific to that instance.
# Instance methods are used for operations that require access to instance-specific data.