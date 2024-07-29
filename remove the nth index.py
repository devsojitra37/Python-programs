def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n+1:]

    # Return the result by concatenating 'first_part' and 'last_part', effectively removing the character at index 'n'.
    return first_part + last_part

# Call the remove_char function with different input strings and character positions and print the results.
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))
