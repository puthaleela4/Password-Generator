import random
print("Welcome to the password generator")
letters=int(input("How many letters would you like in your password?"))
symbols=int(input("How many symbols would you like?"))
numbers=int(input("How many numbers would you like?"))
rl=""
for letter in range(97,123):
    rl+=chr(letter)
rs=""
sym=[33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,96,123,124,125,126]
for symbol in sym:
    rs+=chr(symbol)
rn=""
for number in range(1,100):
    rn+=str(number)
a=random.sample(rl,letters)
b=random.sample(rs,symbols)
c=random.sample(rn,numbers)
password=a+b+c
random.shuffle(password)
e="".join(password)
print(e)
