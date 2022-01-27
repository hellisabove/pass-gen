#!/usr/bin/env python3
import random
import string

length = int(input('Enter length of password: '))

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num   = string.digits
symbols = string.punctuation

#combine the data
all = lower+upper+num+symbols

#randomize beetwen data and length
temp = random.sample(all,length)

#create the password
password = "".join(temp)

f= open("password.txt","w+")
f.write(password)
f.close()

print('Your password, ' + password + ' has been saved in the file password.txt')
