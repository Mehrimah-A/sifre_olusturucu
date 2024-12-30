karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
import random

def generate_password(numOfChars):
    password=""
    for i in range(numOfChars):
        password+=random.choice(karakterler)
    return password

number_of_letters=int(input("kac karakterli bir sifre istiyorsun?"))

password=generate_password(number_of_letters)

print(password)