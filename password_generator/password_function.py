import random 
import string
from flask import Flask, render_template,request 
line1 = string.ascii_letters
line2 = string.digits
line3 = string.punctuation
def generate_password(length):
    characters = line1+line2+line3
    password = ''
    for _ in range(length):
        word = random.choice(characters)
        password = password + word

    return password

#print(generate_password(14))
#print(generate_password(20))
my_password = generate_password(20)
print(my_password)



