print("Kimlik(ID) değiştiren durumlar:\n","*"*50,"\n",sep='')

liste1 = [1, 2, 3]
print("Başlangıç listesi:", liste1)
print("Kimlik (id):", id(liste1))

liste1.append(4)        # Yeni eleman ekler, kimlik değişmez
print("\n.append sonrası:", liste1)
print("Kimlik (id):", id(liste1))

liste1.remove(2)        # Bir eleman çıkarır, kimlik değişmez
print("\n.remove sonrası:", liste1)
print("Kimlik (id):", id(liste1))

liste1.sort()           # Listeyi sıralar, kimlik değişmez
print("\n.sort sonrası:", liste1)
print("Kimlik (id):", id(liste1))


print("\nKimlik(ID) değiştiren durumlar:\n","*"*50,"\n",sep='')

liste2 = [1, 2, 3]
print("Başlangıç listesi:", liste2)
print("Kimlik (id):", id(liste2))

# Yeni bir liste ataması yapıldığında
liste2 = liste2 + [4]   # Yeni bir liste oluşur, kimlik değişir
print("\n+ operatörü sonrası:", liste2)
print("Kimlik (id):", id(liste2))

# Dilim alındığında
liste2 = liste2[:2]     # Yeni bir liste oluşur, kimlik değişir
print("\nDilim sonrası:", liste2)
print("Kimlik (id):", id(liste2))

# Çoğaltma operatörü kullanıldığında
liste2 = liste2 * 2     # Yeni bir liste oluşur, kimlik değişir
print("\n* operatörü sonrası:", liste2)
print("Kimlik (id):", id(liste2))
