import random
import string

characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
length = 16

password = ''.join(random.choice(characters) for _ in range(length))
print(password)
