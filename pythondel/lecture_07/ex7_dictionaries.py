# Dictionary - items are stored as key-value pairs.

# For example, in an address book, the names are the keys,
# and the values are the address.

# Note the use of { } and :
address_book = {
    "Emma": "Storgatan 12, Stockholm",
    "Liam": "Västra Hamngatan 5, Göteborg",
    "Fatima": "Möllevångsgatan 8, Malmö",
    "Erik": "Kungsgatan 20, Uppsala",
    "Amina": "Östra Förstadsgatan 15, Lund",
    "Johan": "Drottninggatan 3, Örebro"
}

# Suppose we want to get (read) someone's address.
# We use the persons name (key) to retrieve the address (value):
print(address_book["Emma"])

# If someone moves house, we can update the address (value) for that name (key)
address_book["Emma"] = "Nordmannavägen 23, Lund"

# Dictionaries also have a length:
print(len(address_book))

# Strings are often used as keys, but the value can be any type, like floating-point numbers:
sweet_prices = {
    "Geléhallon": 12,
    "Skumsvampar": 20,
    "Ahlgrens bilar": 20,
    "Polkagrisbitar": 25,
    "Lakritsbitar": 10
}

print( sweet_prices["Skumsvampar"] + sweet_prices["Polkagrisbitar"] )

# Keys need to be unique, but not values.