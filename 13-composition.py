class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        self.engine.start()
# Create an instance of Engine
engine = Engine()
# Create an instance of Car with the engine
car = Car(engine)
# Start the car 
car.start_car()  # Output: Engine started
# In this example, the Car class has a composition relationship with the Engine class.
# The Car class contains an instance of the Engine class, allowing it to use the engine's functionality.
# Composition is a design principle where one class contains another class as a member
    