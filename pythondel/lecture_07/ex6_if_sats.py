
# Does our new password meet complexity requirements?
new_password = "fhr9ehfh"

if len(new_password) >= 8:
    print("Strong password")
else:
    print("Weak password")

# Note again the use of indentation!

exam_score = 45
if exam_score >= 50:
    print("Pass")
else:
    print("Fail")



# In this case, we put the if statement into a function:
def print_shipping_cost_message(total):
    has_free_shipping = total >= 50
    if has_free_shipping:
        print("Free shipping")
    else:
        print("Shipping costs apply")

    print("now the function is finished!")

print_shipping_cost_message(40)
print_shipping_cost_message(60)


