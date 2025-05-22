# Step 1: Define the decorator
def log_function_call(func):
    def wrapper():
        print("Function is being called")  # logging BEFORE actual call
        return func()  # calling the actual function
    return wrapper

# Step 2: Apply the decorator to say_hello
@log_function_call
def say_hello():
    print("Hello, world!")

# Step 3: Call the function
say_hello()

# Decorators are just functions that wrap other functions. Imagine a gift wrapped in glittery paper—that’s your normal function wearing extra sparkle.
# @log_function_call is basically short form for say_hello = log_function_call(say_hello). It’s like saying, “Hey, before you do your thing, let’s add some extra flair!”