liste = ["abc", 34, (7,4)]
print(liste[2])
#0.indis  = abc
#1.indis = 34
#2.indis = 7,4

notlar= [30,50,80,90]
liste= ["a", 10, 20, notlar]
print(liste)
print(type(liste))  #tipini döndürür
print(len(liste))   #uzunluğunu verir. a, 10, 20, notlar 4 döner
print(type(liste[0]))   #0. indisin tipi a olduğu için string
print(type(liste[1]))   #1. indisin tipi 10 olduğu için int


#İki listeyi birleştirme:
isim= ["x", 10,80, 6.5]
birlestir=[isim,liste]
print(birlestir)


#İndeks dışı değer: liste[9]
liste = ["a","b","c","d","e"]
print(liste[0:2]) #a,b - 0dan 2ye kadar olan indisler
print(liste[ :2]) #2den önceki indisler
print(liste[2: ]) #2den sonraki indisler

liste=["h",10,3.2,50,[1,2,3]]
#liste içerisindeki bir elemanın içine erişim: 
print(liste[4][2]) #4.indis = [1,2,3] 2.indis 2






#liste elemanı değiştirme:
liste = ["ali", "veli", "celil"]
liste[1] = "ahmet"   #indisi 1 olan veliyi ahmet yaptı
print(liste)


#birden fazla eleman değiştirme:
liste = ["ali", "veli", "celil"]
liste[0:3]
liste[0:3]="Merve","Kemal","Defne" #3.indise olan verileri değiştir, 0 ali, 1 veli, 2 celil
print(liste)
liste = liste + ["cansu"]   #cansu ekledim
print(liste)
del (liste[3])              #cansu sildim
print(liste)