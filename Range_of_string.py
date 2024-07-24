def check_range(s):
    if len(s) < 1 or len(s) > 100:
        return False
    for c in s:
        if not ('a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9' or c == ' '):
            return False
    return True

s = input("Enter a string: ")
if check_range(s):
    print(s, "is in the valid range.")
else:
    print(s, "is not in the valid range.")