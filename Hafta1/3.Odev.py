import random
b=[]
for i in range(6):
    b.append(random.randrange(1, 49))
sayac=5
a=[]
cevap=[]
while sayac >= 0:
    a.append(input("Tahmin girini: "))
    sayac=sayac-1

for i in range(6):
    if int(b[i]) == int(a[i]):
        cevap.append(b[i])
    else:
        cevap.append("-")
print("Doğru bildiğiniz cevaplar: ",cevap)
    
