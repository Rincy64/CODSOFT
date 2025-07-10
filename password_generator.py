import random
import string

def generate_password(length):
  if length<4:
    return "Password length must be at least 4 characters."
    characters = string.ascii_letters+string.digits+string.punctuation
    password+=random.choices(characters,k=length-4)
    random.shuffle(password)
    return''.join(password)
  try:
    user_length=int(input("Enter the desired password login:"))
    password=generate_password(user_length)
    print("Generated Password:",password)
  except ValueError:
    print("Please enter a valid number.")
      
