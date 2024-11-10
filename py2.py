i1=input("bir tamsayı giriniz:")
i2=input("bir tamsayı daha giriniz:") #burdaki inputlar girilen ifadeleri string ifade olarak tanıyor
s=i1+i2

print(s)#9 , 11 gibi sayılar girilirse bunları bitişik biçimde 911 yazdırır

j=int(input("kaç defa yazılsın?\n"))
for i in range(j+1):
    print(f"{i} kere yazıldı\n"*i)