class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The object itself is the iterator

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Signals the loop to stop here StropIteration is a built-in exception in Python that is raised to indicate that there are no further items produced by the iterator.
        else:
            value = self.current
            self.current -= 1  # Countdown by 1
            return value

# Testing the countdown
for number in Countdown(5):
    print(number)
