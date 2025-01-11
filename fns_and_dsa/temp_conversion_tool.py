FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def is_valid_temperature(temperature):
    return temperature.replace('.', '', 1).isdigit()

while True:
    temperature = input("Enter the temperature to convert: ")
    if is_valid_temperature(temperature):
        temperature = float(temperature)
        break
    else:
        print("Invalid temperature. Please enter a numeric value.")


factor = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if factor.upper() == "C":
    print(f"{temperature}°C  is {convert_to_fahrenheit(temperature)}°F")
elif factor.upper() == "F":
    print(f"{temperature}°F  is {convert_to_celsius(temperature)}°C")
