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

BankaHesabi.bakiyeGoruntule(bankahesabi1)
BankaHesabi.paraYatir(bankahesabi1,100000)

BankaHesabi.paraCek(bankahesabi1,2000000)
BankaHesabi.bakiyeGoruntule(bankahesabi1)
