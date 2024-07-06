FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

temperature = int(input("Enter the temperature to convert: "))
check = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if check == "F":
    convert_to_c = convert_to_celsius(temperature)
    print(f"{temperature}\u00B0F is {convert_to_c}\u00B0C")
elif check == "C":
    convert_to_f = convert_to_fahrenheit(temperature)
    print(f"{temperature}\u00B0C is {convert_to_f}\u00B0F")
    
    
else:
    print("Invalid temperature. Please enter a numeric value.")
