# Using booleans in an if statement in Python

variable = True

# ✅ check if a variable has a boolean value of True
if variable is True:
    # 👇️ this runs
    print('The boolean is True')

# ------------------------------------------

# ✅ check if a variable is truthy
if variable:
    # 👇️ this runs
    print('The variable stores a truthy value')