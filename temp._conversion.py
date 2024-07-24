def convert_temp(temperature, unit):
    if unit == 'C':
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit
    elif unit == 'F':
        celsius = (temperature - 32) * 5/9
        return celsius
    else:
        return "Invalid unit. Please enter either 'C' for Celsius or 'F' for Fahrenheit."

# get user input
temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C or F): ")

# call function and print result
result = convert_temp(temperature, unit)
print(result)