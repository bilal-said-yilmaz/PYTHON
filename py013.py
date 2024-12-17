class Araba:
    def __init__(self,marka,model,hiz):
        self._marka=marka # _ ifadesi erişilecek nesneye protected özelliği katıyor erişimi kısmen kısıtlıyor
        self._model=model
        self._hiz=hiz
    def arabaGoster(self):
        return f'Markası:{self._marka}\t Modeli:{self._model}\t Maximum hızı:{self._hiz}km/sa\n'
araba1=Araba("Mazda","RX7",251)

print(araba1.arabaGoster())

araba1._hiz=333 # Bu şekilde erişilebilir fakat önerilen bir özellik değildir
print(araba1._hiz) # Aynı şekilde erişilebilir fakat önerilen bir özellik değildir
