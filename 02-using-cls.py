class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")
# Create instances of Counter
counter1 = Counter()
counter2 = Counter()    
counter3 = Counter()
# Display the count of objects created
Counter.display_count()  # Output: Total objects created: 3
# The class method display_count is called on the class itself, not on an instance.
# This is useful for keeping track of class-level data.
