"""
Temperature Converter Module
Provides functions to convert between Celsius, Fahrenheit, and Kelvin.
"""
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

"""
Convert temperature from Celsius to Fahrenheit.

Args:
celsius (float): Temperature in Celsius

Returns:

float: Temperature in Fahrenheit

Example:
celsius_to_fahrenheit(0)
Sensitivity: Internal
32.0
celsius_to_fahrenheit(100)
212.0
"""

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
"""
Convert temperature from Fahrenheit to Celsius.

Args:
fahrenheit (float): Temperature in Fahrenheit

Returns:

float: Temperature in Celsius

Example:
fahrenheit_to_celsius(32)
0.0
fahrenheit_to_celsius(212)
100.0
"""

    
def celsius_to_kelvin(celsius):
    return celsius + 273.15
"""
Convert temperature from Celsius to Kelvin.
Args:
celsius (float): Temperature in Celsius
Returns:
float: Temperature in Kelvin
Example:
>>> celsius_to_kelvin(0)
273.15
"""

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
"""
Convert temperature from Kelvin to Celsius.
Args:
kelvin (float): Temperature in Kelvin
Returns:
float: Temperature in Celsius
Sensitivity: Internal
Example:
kelvin_to_celsius(273.15)
0.0
"""

if __name__ == "__main__":
# Quick test of conversion functions
    print("Temperature Converter Tests")
    print(f"0°C = {celsius_to_fahrenheit(0)}°F")
    print(f"100°C = {celsius_to_fahrenheit(100)}°F")
    print(f"0°C = {celsius_to_kelvin(0)}K")