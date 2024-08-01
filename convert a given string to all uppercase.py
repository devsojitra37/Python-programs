def to_uppercase(str1):
    # Initialize a variable 'num_upper' to count the uppercase letters in the first 4 characters of 'str1'.
    num_upper = 0

    # Iterate through the first 4 characters of 'str1'.
    for letter in str1[:4]:
        # Check if the uppercase version of the letter is the same as the original letter.
        if letter.upper() == letter:
            # If they are the same, increment the 'num_upper' count.
            num_upper += 1

    # Check if the count of uppercase letters is greater than or equal to 2.
    if num_upper >= 2:
        return str1.upper()

    return str1

print(to_uppercase('Tonino'))
print(to_uppercase('ToNino'))
