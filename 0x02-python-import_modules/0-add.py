#!/usr/bin/python3
# Assign the values to variables a and b
a = 1
b = 2

# Define the add function
exec(open('add_0.py').read())

# Print the result of the addition
print('{} + {} = {}'.format(a, b, add(a, b)))
