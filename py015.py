class Calisan:
    def __init__(self,tamAdi,yasi,maasi):
        self.tamAdi=tamAdi
        self.yasi=yasi
        self.__maasi=maasi
    def maasGuncelle(self,yeniMaas):
        if yeniMaas > 0:
            self.__maasi=yeniMaas
            print(f"{self.tamAdi} adlı çalışanımızın maaşı güncellenmiştir")
        else:
            print("Hatalı maaş girişi")
    def calisanGoster(self):
        return f"{self.tamAdi} adındaki çalışanımızın yaşı: {self.yasi}, maaşı: {self.__maasi}₺"

class KidemliCalisan(Calisan):
    def __init__(self,tamAdi,yasi,maasi,pozisyonu):
        super().__init__(tamAdi,yasi,maasi)
        self.__pozisyonu=pozisyonu
    def pozisyonGoster(self):
        return f"{self.tamAdi} adındaki çalışanımızın pozisyonu: {self.__pozisyonu}"
    def pozisyonGuncelle(self,yeniPozisyon):
        self.__pozisyonu=yeniPozisyon
        print(f"{self.tamAdi} adlı çalışanımızın pozisyonu güncellenmiştir")
    
calisan1=KidemliCalisan("Ali Al",28,70000,"Takım Lideri")
calisan2=KidemliCalisan("Atalay At",33,90000,"Proje Yöneticisi")
calisan3=Calisan("Ayşe Ay",23,17002)

print(calisan1.calisanGoster())
print(calisan2.calisanGoster())
print(calisan3.calisanGoster())
print("*"*55)

calisan3.maasGuncelle(25503)
print(calisan3.calisanGoster())
print("*"*55)
# calisan3.pozisyonGoster() bu kısım çalışmayacak çünkü bu zavallı çalışanın bir pozisyonu yok 
print(calisan1.pozisyonGoster())
print("*"*55)
calisan2.pozisyonGuncelle("Operasyon Sorumlusu")
print(calisan2.pozisyonGoster())
