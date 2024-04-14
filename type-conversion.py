x = input("1.sayı:")
y = input("2.sayı:")
toplam = x + y
print(toplam)
#toplamadı yan yana yazdı çüünkü inputtan gelen bilgi hep stringtir

print(type(x))
print(type(y))
toplam = int(x) + int(y)
print(toplam)
#şimdi topladı

x = float(x)
print(x)