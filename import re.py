import re

def validate_password(pwd):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#]).{8,}$'
    return re.match(pattern, pwd) is not None

# Create the input file automatically
sample = ["Parth@123", "hello123", "ABCdef#9", "Short1@", "Password123"]
with open("passwords.txt", "w") as f:
    f.write("\n".join(sample))

# Read passwords from file
with open("passwords.txt", "r") as f:
    passwords = f.read().splitlines()

# Validate and write results
with open("result.txt", "w") as out:
    for p in passwords:
        status = "Valid" if validate_password(p) else "Invalid"
        print(f"{p:<15} -> {status}")
        out.write(f"{p} -> {status}\n")