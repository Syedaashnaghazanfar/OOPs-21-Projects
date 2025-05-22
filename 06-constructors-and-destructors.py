class Logger:
    def __init__(self):
        print("Logger initialized")

    def __del__(self):
        print("Logger destroyed")

# Create an instance of Logger
logger = Logger()
# The __init__ method is called when the object is created, initializing the object.
# The __del__ method is called when the object is about to be destroyed, allowing for cleanup.
# In this case, it prints a message indicating that the logger is being destroyed.
# The __del__ method is not guaranteed to be called immediately when the object goes out of scope.
# It is called when the object is garbage collected, which may not happen immediately.