sayi = int(input("Beş ve üzeri basamağa sahip sayı giriniz : "))  
sayi1 = sayi  
ters = 0
basamak=0
while (sayi1>0):
    basamak+=1
    sayi1 //=10
if basamak >=5:   
    while(sayi > 0):    
        gecici = sayi %10    
        ters = (ters *10) + gecici    
        sayi = sayi //10    
    print("Sayının son hali = %d" %ters)
else:
    print("Hatalı giriş")
 