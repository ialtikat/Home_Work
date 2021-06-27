yasak=["merhaba","araba","dünya","köpek"]
cumle=input("Bir cümle giriniz: ")
kelime=cumle.split()
nesne=""
for i in range(len(kelime)):
    c=""
    for j in range(len(yasak)):
        if kelime[i].count(yasak[j]) == True:
            a=list(kelime[i])
            b=len(yasak[j])
            for k in range(b):
                a[k] = "*"
            for x in range(len(a)):
                c=c+a[x]
            kelime[i]=c
for i in range(len(kelime)):
    nesne=nesne+kelime[i]+" "
print(nesne)