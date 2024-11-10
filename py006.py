def f(y): # buraya argüman olarak x gönderilseydi ve altta global olarak alınsaydı burda karışıklık olur ve hata döner
    global x
    print(x)
    # x=5 sqope dışında değişken okunabilir fakat değiştirilemez
    x=-1
    print(x+1)
    # y=0 öncelikle sqopeda varsa depişken o esas alınır daha sonra argüman olarak gönderilen değer ona da ulaşılamazsa global değişkenlere ulaşılır
x=12
y=90
f(y) 
donusdegeri=f(y)
print(y)
print(x)
print(donusdegeri) # none döner çünkü return kullanmadığımızdan default olarak boş döner

# immutable veri yapıları olan int,float,boolean,strings ve tuples
# mutable olan veri yapıları ise lists , dictionaries ve sets

# immutable veri yapıları değiştirilemez olduğundan dolayısıyla yeni değer ataması yapıldığında bu değişken için yeni obje oluşur
#                                                                          ve gösterdiği referans değeri yani id'si değişmiş olur
# mutable olan listleri ele aldığımızda ise içerisinden bir indeksteki değeri değiştirdiğimizde o listin id'si değişmez 
# sadece o indeksteki değikenin tuttuğu referans değeri değişir

# Başlangıç listesi
liste = [10, 20, 30]
print(f"Başlangıç Liste ID: {id(liste)}")
print(f"Başlangıç Liste: {liste}")
print(f"Liste[0] ID: {id(liste[0])}")
print(f"Liste[1] ID: {id(liste[1])}")
print(f"Liste[2] ID: {id(liste[2])}")

# Eleman değiştirme
liste[1] = 200
print("\nEleman değiştirdikten sonra:")
print(f"Liste ID: {id(liste)}")  # Aynı kalmalı
print(f"Liste: {liste}")
print(f"Liste[1] ID: {id(liste[1])}")  # Değişmeli

# Aynı değeri atama
liste[0] = 10
print("\nAynı değeri atadıktan sonra:")
print(f"Liste ID: {id(liste)}")  # Aynı kalmalı
print(f"Liste: {liste}")
print(f"Liste[0] ID: {id(liste[0])}")  # Aynı kalmalı

# Farklı bir tip atama
liste[2] = "Otuz"
print("\nFarklı bir tip atadıktan sonra:")
print(f"Liste ID: {id(liste)}")  # Aynı kalmalı
print(f"Liste: {liste}")
print(f"Liste[2] ID: {id(liste[2])}")  # Değişmeli
