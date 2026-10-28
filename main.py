import re

# Read the text file
with open("input.txt", "r") as file:
    text = file.read()

# Regex pattern for email addresses
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Find all matching emails
emails = re.findall(pattern, text)

# Display results
if emails:
    print("Email addresses found:")
    for email in emails:
        print(email)
else:
    print("No email addresses found.")