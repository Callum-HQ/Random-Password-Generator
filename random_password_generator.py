import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
  length = int(input("Enter your desired password length: "))

  alphabets_number = int(input("Enter the minimum number of letters you want in your password"))
  digits_number = int(input("Enter the minimum number of digits you want in your password"))
  special_characters_number = int(input("Enter the minimum number of special characters you want in your password"))

  number_characters = alphabets_number + digits_number + special_characters_number

  if number_characters > length:
    print("Sorry, the total number of alphabets, digits and special characters exceed your desired password length.")
    return

  password = []

  for i in range(alphabets_number):
    password.append(random.choice(alphabets))
    
  for i in range(digits_number):
    password.append(random.choice(digits))
    
  for i in range(special_characters_number):
    password.append(random.choice(special_characters))

  if number_characters < length:
    random.shuffle(characters)
    for i in range(length - number_characters):
      password.append(random.choice(characters))

  random.shuffle(password)

  print("".join(password))

generate_random_password()