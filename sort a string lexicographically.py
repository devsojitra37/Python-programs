# Define a function named lexicographic_sort that takes one argument, 's'.
def lexicographic_sort(s):
    # Use a nested sorting approach:
    # 1. First, sort the characters of the string 's' in ascending order.
    # 2. Then, sort the sorted characters based on their uppercase representations (case-insensitive).
    return sorted(sorted(s), key=str.upper)

# Call the lexicographic_sort function with different input strings and print the results.
print(lexicographic_sort('hublot'))
print(lexicographic_sort('jacob&co'))
