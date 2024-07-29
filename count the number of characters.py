
def char_frequency(str1):
    dict = {}

    for n in str1:
        # Retrieve the keys (unique characters) in the 'dict' dictionary.
        keys = dict.keys()

        # Check if the character 'n' is already a key in the dictionary.
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1

    # Return the dictionary containing the frequency of each character in the input string.
    return dict

# Call the char_frequency function with the argument 'google.com' and print the result.
print(char_frequency('google.com'))
