def change_char(str1):
    # Get the first character of the input string 'str1' and store it in the variable 'char'.
    char = str1[0]

    # Replace all occurrences of the character 'char' with '$' in the 'str1' string.
    str1 = str1.replace(char, '$')

    # Reconstruct the 'str1' string by placing the original 'char' as the first character
    # followed by the modified string starting from the second character.
    str1 = char + str1[1:]

    return str1

print(change_char('restart'))
