#!/usr/bin/python3
# Assign the value 1 to variable a
a = 1

# Assign the value 2 to variable b
b = 2

# Define the add function using the content of add_0.py
add_code = """
def add(a, b):
    \"\"\"My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    \"\"\"
    return (a + b)
"""
add = {}
exec(add_code, add)

# Print the result of the addition using string formatting
print('{} + {} = {}'.format(a, b, add['add'](a, b)))
