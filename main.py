import random
import time

pass_len = int(input("Enter the length of password"))
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
chara = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

comlist = digit + chara + symbols

rand_digit = random.choice(digit)
rand_chara = random.choice(chara)
rand_symbols = random.choice(symbols)

tpass = rand_symbols + rand_chara + rand_digit
print(tpass)
for _ in range(pass_len - 3):
    tpass = tpass + random.choice(comlist)

final_pass = ""
for i in range(pass_len):
    final_pass = final_pass + random.choice(tpass)

print(final_pass)
