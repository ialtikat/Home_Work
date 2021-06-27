myList=[
    {'Ders':"Fonksiyonel Prog",'isim':("Oğuz","Mehmet"),'vize':(14,23),'final':(55, 30),'proje':(99,65)},
    {'Ders':"Algo Prog",'isim':("Oğuz","Mehmet"),'vize':(52,16),'final':(32,33),'proje':(79,85)},
    {'Ders':"Ağ Prog",'isim':("Oğuz","Mehmet"),'vize':(32,40),'final':(55,50),'proje':(95,75)}
    ]


for i in range(len(myList)):
    vize=myList[i]['vize']
    final=myList[i]['final']
    proje=myList[i]['proje']

    vize = [j*0.3  for j in vize]
    final = [j*0.5  for j in final]
    proje = [j*0.2  for j in proje]
    ortalama=[]

    k=0
    while k<2:
        ortalama.append(vize[k]+final[k]+proje[k])
        k+=1
    myList[i]["ortalama"]= tuple(ortalama)
    ort = float("{:.2f}".format(sum(myList[i]["ortalama"])/len(myList[i]["ortalama"])))
    ortsira=[]
    ortsira.append(ort)
    durum = []
    for k in ortalama:
        if (k < ort):
            durum.append("kaldi")
        else:
            durum.append("gecti")

    myList[i]["durum"]=tuple(durum)
for i in range(len(myList)):
    print(">",myList[i])