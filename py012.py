class BankaHesabi:
    def __init__(self,hesapSahibi,turu,bakiye=0):
        self.hesapSahibi=hesapSahibi
        self.turu=turu
        self.bakiye=bakiye

    def paraYatir(self,miktar):
        self.bakiye+=miktar
        return self.bakiye

    def paraCek(self,miktar):
        self.bakiye-=miktar
        return self.bakiye

    def bakiyeGoruntule(self):
        print(f'{self.hesapSahibi} adlı kullanıcının bakiyesi: {self.turu}{self.bakiye}')

bankahesabi1=BankaHesabi("Elon Musk","$",439400000000)

bankahesabi1.bakiyeGoruntule()
bankahesabi1.paraYatir(100000)

bankahesabi1.paraCek(2000000)
bankahesabi1.bakiyeGoruntule()
