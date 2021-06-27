import random 
dicxy={}
liste=[[0 for x in range(15)] for x in range(15)] #Matrisi oluşturma
for i in range(15):
    print(liste[i])
for i in range(45):
    dicxy[random.randint(0,14)]=random.randint(0,14)
try:
    while True:
        tahminx=int(input("X ekseni giriniz: "))
        tahminy=int(input("Y ekseni giriniz: "))
        if dicxy[tahminx]==tahminy:
            print("Kaybettiniz")
            break
        elif liste.count(0) == len(dicxy):
            print("Kazandın")
            break
        else:
            liste[tahminx][tahminy]=1
            for i in range(15):
                print(liste[i])
except:
    print("Hata!!!")