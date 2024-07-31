# Define a function named insert_end that takes one argument, 'str'.
def insert_end(str):
    # Extract the last two characters from the input string 'str' and store them in 'sub_str'.
    sub_str = str[-2:]

    return sub_str * 4

# Call the insert_end function with different input strings and print the results.
print(insert_end('Python'))
print(insert_end('Language'))
