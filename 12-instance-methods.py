class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9
    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15
    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15
 # Example usage
temp_in_celsius = 25
temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_in_celsius)
temp_in_kelvin = TemperatureConverter.celsius_to_kelvin(temp_in_celsius)
print(f"{temp_in_celsius}°C = {temp_in_fahrenheit}°F")  # Output: 25°C = 77.0°F 
print(f"{temp_in_celsius}°C = {temp_in_kelvin}K")  # Output: 25°C = 298.15K
temp_in_fahrenheit = 77
temp_in_celsius = TemperatureConverter.fahrenheit_to_celsius(temp_in_fahrenheit)
print(f"{temp_in_fahrenheit}°F = {temp_in_celsius}°C")  # Output: 77°F = 25.0°C
temp_in_kelvin = 298.15
temp_in_celsius = TemperatureConverter.kelvin_to_celsius(temp_in_kelvin)
print(f"{temp_in_kelvin}K = {temp_in_celsius}°C")  # Output: 298.15K = 25.0°C
# The TemperatureConverter class provides static methods for converting temperatures between Celsius, Fahrenheit, and Kelvin.
# Static methods are used here because the conversion formulas do not depend on instance-specific data.
# They can be called directly on the class without creating an instance.
# Static methods are useful for utility functions that perform operations related to the class but do not require access to instance or class variables.