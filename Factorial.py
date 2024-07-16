num = int(input("Enter a number: "))

if num < 0:
    print("Invalid number. Please enter a non-negative number.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)