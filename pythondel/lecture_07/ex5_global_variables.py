balance = 1000

# In this function, we want to modify the variable 'balance', which is used outside the function.
# So we need to explicitly make the variable 'global'.
def deposit(amount):
    global balance
    balance = balance + amount

def withdraw(amount):
    global balance
    balance = balance - amount

deposit(200)
withdraw(150)

print(balance)