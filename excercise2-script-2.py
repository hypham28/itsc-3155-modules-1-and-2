# Get input from the user
user_input = input("Enter a string: ")

# Initialize variables to store lowercase and uppercase letters
lowercase_letters = ""
uppercase_letters = ""

# Iterate through the input string
for char in user_input:
    if char.islower():
        # If it's a lowercase letter, add it to the lowercase_letters variable
        lowercase_letters += char
    elif char.isupper():
        # If it's an uppercase letter, add it to the uppercase_letters variable
        uppercase_letters += char

# Print the lowercase letters followed by the uppercase letters
print(lowercase_letters + uppercase_letters)
