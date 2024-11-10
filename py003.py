sayi1=int(input())
sayi2=int(input())
sayi3=int(input())
enbuyuk=0
enkucuk=0

# Basitçe şöyle de yapabilirdik
enbuyuk=sayi1
enkucuk=sayi1
if sayi2>enbuyuk:
    enbuyuk=sayi2
    if sayi3<sayi1:
        enkucuk=sayi3
elif sayi3>enbuyuk:
    enbuyuk=sayi3
    if sayi2<sayi1:
        enkucuk=sayi2

""" if sayi1>sayi2:
    if sayi1>sayi3:
        enbuyuk=sayi1
        if sayi2>sayi3:
            enkucuk=sayi3
        else:
            enkucuk=sayi2
    else:
        enbuyuk=sayi3

elif sayi2>sayi3:
    if sayi2>sayi3:
        enbuyuk=sayi2
        if sayi1>sayi3:
            enkucuk=sayi3
        else:
            enkucuk=sayi1
    else:
        enbuyuk=sayi3
else:
    enbuyuk=sayi3
    if sayi1>sayi2:
            enkucuk=sayi2
    else:
        enkucuk=sayi1 """

print(f"en küçük değer: {enkucuk}\nen büyük değer:{enbuyuk}") 
#print("en küçük değer: {enkucuk}\nen büyük değer:{enbuyuk}")  FORMATSIZ HALİNİ YAZARSAK DEĞİŞKENLERİ ALGILAMAZ

