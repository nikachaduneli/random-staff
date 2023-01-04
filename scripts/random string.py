import random


simbols = []

to_Code = dict()

for i in range(33,127):

    simbols.append(chr(i))

print(simbols)

for i in simbols:
    code = ''
    values =  list(to_Code.values())
    for j in range(random.randint(2, 4)):
        code += random.choice(simbols)
    if values.count(code) == 0:
        to_Code[i] = code

print(to_Code)