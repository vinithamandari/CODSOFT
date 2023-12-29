# prompt: to create a password generator application using Python, allowing users to  specify the length and complexity of the password

import random
import string

def generate_password(length, complexity):
  # Create a list of all possible characters
  characters = list(string.ascii_lowercase)
  if complexity == "medium":
    characters.extend(string.ascii_uppercase)
  elif complexity == "high":
    characters.extend(string.ascii_uppercase + string.digits + string.punctuation)

  # Generate a random password
  password = ""
  for i in range(length):
    password += random.choice(characters)

  # Return the password
  return password

# Get the user's input
length = int(input("Enter the length of the password: "))
complexity = input("Enter the complexity of the password (low, medium, high): ")

# Generate the password
password = generate_password(length, complexity)

# Print the password
print("Your password is:", password)