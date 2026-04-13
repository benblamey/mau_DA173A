# Functions:
# - are a named unit of code
# - can be invoked as many times as needed.
# - optionally take one or more input parameters.
# - optionally return a value
# - allow us to define a calculation, or sequence of steps for re-use.
# - help us to structure code, avoid repetition.
# - we can define our own functions with the def keyword

# declare the function for future use.
# the function is not executed here!
def is_18_or_over(age):
    result = age >= 18
    return result

# Note how Python uses indentation (not braces like in Javascript)

age_in_years = 23
print("Is over 18?:")
return_value = is_18_or_over(age_in_years) # Invoke the function
print(return_value)


age_in_years = 35
print("Is over 18?:")
print(is_18_or_over(age_in_years))


def square(x):
    return x * x

x_squared = square(3)
print(x_squared)

# What's the output here? How many times is the function invoked?
print(square(square(2)))