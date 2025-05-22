# Step 1: Create custom exception class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older."):
        super().__init__(message)

# Step 2: Define a function that checks age and raises the exception if invalid
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older!")
    else:
        print(f"Age {age} is valid. You may proceed.")

# Step 3: Use try...except to handle the exception
# try:
#     check_age(16)  # Test with invalid age
# except InvalidAgeError as e:
#     print(f"Caught an exception: {e}")

try:
    check_age(21)  # Test with valid age
except InvalidAgeError as e:
    print(f"Caught an exception: {e}")
