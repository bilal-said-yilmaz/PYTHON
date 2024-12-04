# List Comprehensions 
liste1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
liste2=[sayi for sayi in liste1 if sayi%2==0]
print(liste1)
print(liste2)

# List Slicing
liste3=liste1[::] # Tüm listeyi gezer ve yeni listemize atar 
print(liste3)

liste3=liste1[:13:2] # 0 dahil 13 dahil değil 0'dan başlayarak 2'şer adım atlayarak yeni listeye atama yapar
print(liste3)

liste3=liste1[13:3:-1] # 13 dahil 3 dahil değil 13'ten geriye doğru 1'er adım yeni listemize atama yapar
print(liste3)

liste3=liste1[1:11:-1] #boş liste döndürür çünkü başlangıçtan bitiş değerine doğru azalarak gidecekken burada başlangıç<bitiş olarak verilmiş
print(liste3)
