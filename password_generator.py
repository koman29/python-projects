import random
import string

passwordLength = int(input("Please enter the length of the password: "))

allowedChars = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(allowedChars) for _ in range(passwordLength))

print(password)
