ogrenciler = []
alinandeger = 0
resim = []
muzik = []
tiyatro = []

print("8 öğrencinin isimlerini giriniz:")
for ogrenci in range(8):
    o = input()
    ogrenciler.append(o)

for i in range(12):
    if i < 4:
        alinandeger = int(input())
        resim.append(ogrenciler[alinandeger])
    elif 4 <= i < 8:
        alinandeger = int(input())
        muzik.append(ogrenciler[alinandeger])
    elif 8 <= i < 12:
        alinandeger = int(input())
        tiyatro.append(ogrenciler[alinandeger])

ayrikmi = sorted(set(resim).isdisjoint(set(tiyatro)))
print(ayrikmi)

sadecebiri = sorted(set(resim) ^ set(tiyatro))
print(sadecebiri)

tumu = sorted(set(resim) | set(tiyatro) | set(muzik))
print(tumu)

hicbir = sorted(set(ogrenciler) - set(tumu))
print(hicbir)
