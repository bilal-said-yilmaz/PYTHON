x=10 # <class 'int'>
y=3.0 # <class 'float'>
z="Hello Python"# <class 'str'>
b=False # <class 'bool'>
c=10/7 # 1.43
d=10//7 # 1
e=2**2**3

print(type(x),type(y),type(z),type(b),sep=',',end='\t') # burdaki sep ifadesi değişkenler arasındaki default değer olan 
#bir boşluk kadarlık kısmı değiştirmemizi sağlıyor end ifadesi ise print ifadesinden sonraki default olan \n i değiştirmemizi sağlıyor 

print(f'{c:.2f},{d}') #formatlanmış print ifadesini tırnaklar arasına alıyoruz ve değişkenlerimizi de { }'ler arasına yazıyoruz

print() # bunu end ve for döngüsüyle kullanmak kullanışlıdır basitçe bi alt satıra geçer

print("buraya bir şeyler \
yazdığımızda alta geçer")#buradaki ters slash kaçış karakterimiz ise alt satıra hata almadan geçmemizi sağlıyor

print(e) # üslü ifadeler diğer operatörlerin tersine sağdan sola doğru işlem yapar önce en dıştaki üs alma sonra içe doğru gelir
