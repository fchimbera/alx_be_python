FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input("Enter the temperature to convert: "))
factor = input("Is this temperature in Celsiuc or Fahrenheit? (C/F):  ")

if factor.upper() == "C":
    print(f"{temperature}°C  is {convert_to_fahrenheit(temperature)}°F")
elif factor.upper() == "F":
    print(f"{temperature}°F  is {convert_to_celsius(temperature)}°C")
