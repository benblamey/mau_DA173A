# Strings

my_string = "DA173A"

# strings have a length
print(len(my_string))

# we can obtain a single character from the string (in the same way as a list)
print(my_string[0])

# But, unlike lists, strings are immutable (read only), and cannot be modified.
# This gives an error:
# my_string[3] = "x"

# However, we derive different strings:
print(my_string.lower())

# You will learn many other useful things to do with strings in the w3school exercises:
# 'Formatting' Strings -- i.e. creating a string from values and a template.
# Slicing -- extracting a string from inside another string.
# Converting Strings to other types e.g. "10" (string) --> 10 (integer)
# ...etc