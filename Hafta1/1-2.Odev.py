import random
dizi=["A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "ş", "t", "u", "v", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
b=""
while True:
    for i in range(8):
        b=b+random.choice(dizi)
    if b.islower() == False and b.isupper() == False and b.isdigit() == False:
        print(b)
        break
    else:
        continue
