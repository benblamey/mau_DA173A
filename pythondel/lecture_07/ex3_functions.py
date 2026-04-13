# These functions take one or more arguments, and return values.
# They don't print anything by themselves.

# len(..) computes length:
l = len("hello")

# max(..) of two values:
# the function takes two arguments.
m = max(10, 15)

# absolute value of a number:
a = abs(-6)

# round(..) can also be useful:
x = 23.4
r = round(x)

print(l)
print(m)
print(a)
print(r)

# What output do we expect here? How many functions are used?
y = 25.6
print(round(max(x, y)))

# All these functions are built into Python.
# https://docs.python.org/3/library/functions.html



