class Ogrenci:
    def __init__(self,adi,soyadi,numarasi,sinifi):
        self.__adi=adi
        self.__soyadi=soyadi
        self.__numarasi=numarasi
        self.__sinifi=sinifi
    def sinifGuncelle(self,yeni_sinifi): # methodun adı set_ ile başlasaydı setter methodu olurdu kontrollü güncelleme işlemlerinde kullanılır
        if yeni_sinifi>0:
            self.__sinifi=yeni_sinifi
        else:
            print("Yanlış sınıf girişi")
    def ogrenciGoster(self): # method adı get_ ile başlasaydı getter methodu olurdu
        return f"Tam adı {self.__adi} {self.__soyadi} olan öğrencimizin numarası: {self.__numarasi}, sınıfı ise: {self.__sinifi} \n"

ogrenci1=Ogrenci("Bilal Said","Yılmaz",11111111111,14)

print(ogrenci1.ogrenciGoster())
ogrenci1.sinifGuncelle(15)
print(ogrenci1.ogrenciGoster())
ogrenci1.sinifGuncelle(-3)
