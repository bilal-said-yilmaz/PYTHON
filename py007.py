a=2;b=2
print(a,b,id(a),id(b)) # Pythonda değişkenler değerlerin bulunduğu ID'leri referans alan birer objelerdir 
c=id(a)
a=3;b=3
print(a,b,id(a),id(b)) # bundan dolayı da yeni değer ataması yapıldığında yeni bir obje oluşturulur ve yeni değerin ID'sini refere eder
d=id(b)
print(d-c)
