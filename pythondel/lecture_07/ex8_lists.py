
# We can declare lists:
fruits = ["banana", "apple", "orange"]

# lists have a length:
print(len(fruits))

# We can get an element by its index (starting at zero)
fruit = fruits[0]
print(fruit)

# We can use a "for loop" to iterate through the items:
print("all the fruits:")
for fruit in fruits:
    print(fruit)

# In the exercises, you will also use the range(..) function to generate lists
# of integers which can be, e.g. used as indices into lists.

# We can modify lists:
fruits.append("mango")
fruits.remove("banana")

# Replace an item at its index:
fruits[1] = "grape"

# for debugging, we can print the whole list:
print(fruits)

list_of_numbers = [10, 20, 30]

# We can use a for loop to add up values, for example:
total = 0
for number in list_of_numbers:
    total = total + number

print(total)


# Lists - Summary
# - are an ordered collection of items
# - can be accessed by their index.
# - can be iterated (with a for loop)
# - elements can be added (and removed)