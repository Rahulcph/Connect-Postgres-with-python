import random
line1 = "zxcvbnmlkjhgfdsaqwertyuiopåæø"
line2 = "1234567890"
line3 = "!#¤%&/()=?`*_:;>"
final = line1+line2+line3
password = ''
for i in range(12):
    word = random.choice(final)
    password = password + word
print(password)  

