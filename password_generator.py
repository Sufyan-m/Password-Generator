import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^"
length = int(input("Password length: "))

# A professional, one-line way to generate the password using join and list comprehension
password = "".join(random.choice(chars) for _ in range(length))

print(password)
