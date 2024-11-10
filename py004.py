a =int(input())
b=0
if (a!=0) and (a>0):
    for i in range(2,(a//2+1)):
        if a%i==0:
            b=-1
            break #Eğer bu break ifadesini for döngüsünde kullanmazsak ekstra iş yükü getirir ve biz bunu istemeyiz
        elif a==1:
            b=-2
            break
        print(i)
elif a<0:
    b=-4
else:
    b=-3
if b==0:
    print("a bir asal sayıdır")
elif b==-1:
    print("a bir asal sayı değildir")
elif b==-2:
    print("a bir asal sayı değildir")
elif b==-3:
    print("a sayısı 0'a eşittir")
elif b==-4:
    print("a negatif bir sayıdır")
