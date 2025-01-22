# Comparison operator
# ==: Equal to
# !=: Not equal to
# >: Greater than
# <: Less than
# >=: Greater than or equal to
# <=: Less than or equal to

# temperature = 20
# if temperature >= 30:
#     print("It's a hot day.")
# elif temperature >= 10:
#     print("It's normal day.")
# else:
#     print("It's a cold day.")

name = input("Enter your name? ")
if len(name) <=3:
    print("name must be at least 3 characters.")
elif len(name) >= 50:
    print("name can be maximum of 50 character")
else:
    print("name looks good!")


# Logical operator
# and: Returns True if all conditions are True.
# or: Returns True if at least one condition is True.
# not: Reverses the result of a condition.

good_credit = True
high_income = False

if good_credit and high_income:
    print("Eligible for lone")
else:
    print("Doesn't eligible for lone")