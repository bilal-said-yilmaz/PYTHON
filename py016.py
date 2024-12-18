class KarmasikSayilar:
    def __init__(self,reelKatsayisi,sanalKisimKatsayisi):
        self.reelKatsayisi=reelKatsayisi
        self.sanalKisimKatsayisi=sanalKisimKatsayisi
    def __add__(self,other):
        if((self.sanalKisimKatsayisi + other.sanalKisimKatsayisi)==1):
            return f'{self.reelKatsayisi + other.reelKatsayisi}+i'
        elif((self.sanalKisimKatsayisi + other.sanalKisimKatsayisi)== -1):
            return f'{self.reelKatsayisi + other.reelKatsayisi}-i'
        elif (self.sanalKisimKatsayisi + other.sanalKisimKatsayisi>0):
            return f'{self.reelKatsayisi + other.reelKatsayisi}+{self.sanalKisimKatsayisi + other.sanalKisimKatsayisi}i'
        elif (self.sanalKisimKatsayisi + other.sanalKisimKatsayisi==0):
            return f'{self.reelKatsayisi + other.reelKatsayisi}'
        else:
            return f'{self.reelKatsayisi + other.reelKatsayisi} {self.sanalKisimKatsayisi + other.sanalKisimKatsayisi}i'
    def __sub__(self,other):
        if(self.sanalKisimKatsayisi - other.sanalKisimKatsayisi==1):
            return f'{self.reelKatsayisi - other.reelKatsayisi}+i'
        elif(self.sanalKisimKatsayisi - other.sanalKisimKatsayisi== -1):
            return f'{self.reelKatsayisi - other.reelKatsayisi}-i'
        elif (self.sanalKisimKatsayisi > other.sanalKisimKatsayisi):
            return f'{self.reelKatsayisi - other.reelKatsayisi}+{self.sanalKisimKatsayisi - other.sanalKisimKatsayisi}i'
        elif (self.sanalKisimKatsayisi == other.sanalKisimKatsayisi):
            return f'{self.reelKatsayisi - other.reelKatsayisi}'
        else:
            return f'{self.reelKatsayisi - other.reelKatsayisi}{self.sanalKisimKatsayisi - other.sanalKisimKatsayisi}i'
    
    def __mul__(self,other):
        if(self.reelKatsayisi * other.sanalKisimKatsayisi + self.sanalKisimKatsayisi * other.reelKatsayisi==1):
            return f'{self.reelKatsayisi * other.reelKatsayisi - self.sanalKisimKatsayisi * other.sanalKisimKatsayisi}+i'
        if(self.reelKatsayisi * other.sanalKisimKatsayisi + self.sanalKisimKatsayisi * other.reelKatsayisi== -1):
            return f'{self.reelKatsayisi * other.reelKatsayisi - self.sanalKisimKatsayisi * other.sanalKisimKatsayisi}-i'
        elif(self.reelKatsayisi * other.sanalKisimKatsayisi + self.sanalKisimKatsayisi * other.reelKatsayisi > 0):
            return f'{self.reelKatsayisi * other.reelKatsayisi - self.sanalKisimKatsayisi * other.sanalKisimKatsayisi}+{self.reelKatsayisi * other.sanalKisimKatsayisi + self.sanalKisimKatsayisi * other.reelKatsayisi}i'
        elif (self.reelKatsayisi * other.sanalKisimKatsayisi + self.sanalKisimKatsayisi * other.reelKatsayisi == 0):
            return f'{self.reelKatsayisi * other.reelKatsayisi - self.sanalKisimKatsayisi * other.sanalKisimKatsayisi}'
        else:
            return f'{self.reelKatsayisi * other.reelKatsayisi - self.sanalKisimKatsayisi * other.sanalKisimKatsayisi} {self.reelKatsayisi * other.sanalKisimKatsayisi + self.sanalKisimKatsayisi * other.reelKatsayisi}i'
    
    def __truediv__(self,other):
        paydadaKalan=other.reelKatsayisi * other.reelKatsayisi + other.sanalKisimKatsayisi * other.sanalKisimKatsayisi
        if(other.reelKatsayisi == 0 and other.sanalKisimKatsayisi==0):
            print("Hatalı bölme işlemi. İkinci karmaşık sayıyı değiştirerek tekrar deneyiniz")
        elif((-(self.reelKatsayisi * other.sanalKisimKatsayisi)+self.sanalKisimKatsayisi*other.reelKatsayisi)/paydadaKalan==1):
            return f'{(self.reelKatsayisi * other.reelKatsayisi+self.sanalKisimKatsayisi*other.sanalKisimKatsayisi)/paydadaKalan}+i'
        elif((-(self.reelKatsayisi * other.sanalKisimKatsayisi)+self.sanalKisimKatsayisi*other.reelKatsayisi)/paydadaKalan== -1):
            return f'{(self.reelKatsayisi * other.reelKatsayisi+self.sanalKisimKatsayisi*other.sanalKisimKatsayisi)/paydadaKalan}-i'
        elif(((-(self.reelKatsayisi * other.sanalKisimKatsayisi)+self.sanalKisimKatsayisi*other.reelKatsayisi)/paydadaKalan)>0):
            return f'{(self.reelKatsayisi * other.reelKatsayisi+self.sanalKisimKatsayisi*other.sanalKisimKatsayisi)/paydadaKalan}+{(-(self.reelKatsayisi * other.sanalKisimKatsayisi) + self.sanalKisimKatsayisi * other.reelKatsayisi)/paydadaKalan}i'
        elif(((-(self.reelKatsayisi * other.sanalKisimKatsayisi)+self.sanalKisimKatsayisi*other.reelKatsayisi)/paydadaKalan)<0):
            return f'{(self.reelKatsayisi * other.reelKatsayis+self.sanalKisimKatsayisi*other.sanalKisimKatsayisi)/paydadaKalan}{(-(self.reelKatsayisi * other.sanalKisimKatsayisi) + self.sanalKisimKatsayisi * other.reelKatsayisi)/paydadaKalan}i'
        else:
            return f'{(self.reelKatsayisi * other.reelKatsayisi + self.sanalKisimKatsayisi * other.sanalKisimKatsayisi)/paydadaKalan}'
    def __eq__(self,other):
        return self.reelKatsayisi == other.reelKatsayisi and self.sanalKisimKatsayisi == other.sanalKisimKatsayisi

    def __str__(self):
        if(self.sanalKisimKatsayisi == 1):
            return (str(self.reelKatsayisi)+"+i")
        elif(self.sanalKisimKatsayisi == -1):
            return (str(self.reelKatsayisi)+"-i")
        elif(self.sanalKisimKatsayisi > 0):
            return (str(self.reelKatsayisi)+"+"+(str(self.sanalKisimKatsayisi) +"i"))
        elif(self.sanalKisimKatsayisi <0 ):
            return (str(self.reelKatsayisi)+(str(self.sanalKisimKatsayisi) +"i"))
        elif(self.sanalKisimKatsayisi == 0):
            return (str(self.reelKatsayisi))
        

karmasik1=KarmasikSayilar(3,1)
karmasik2=KarmasikSayilar(1,1)

print(KarmasikSayilar.__add__(karmasik1,karmasik2))
print(KarmasikSayilar.__sub__(karmasik1,karmasik2))
print(KarmasikSayilar.__mul__(karmasik1,karmasik2))
print(KarmasikSayilar.__truediv__(karmasik1,karmasik2))
print(KarmasikSayilar.__eq__(karmasik1,karmasik2))

print(KarmasikSayilar.__str__(karmasik1))
print(KarmasikSayilar.__str__(karmasik2))
