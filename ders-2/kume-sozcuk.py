sozluk={"numara":"120",
	    "ad":"ahmet",
	    "soyad":"demir"}

print(len(sozluk))

sozluk2={"numara":["no",120],
        "ad":["isim","ahmet"],
        "soyad":["son","demir"]}

print(len(sozluk2))


#merveyi getir------------
Sozluk2={"numara":{"no":120,
                  "isim":"ahmet",
                  "son":"demir"},
        "deger":{"no":100,
                 "isim":"merve",
                 "son":"kara"}}

print(Sozluk2["deger"]["isim"])

#Sozluk[0]  sıralı olmadığından dolayı hata verir. -------> Sozluk["numara"]


#-------------------------------------------------------------------------------------------


l=[1,"a","ali",123]    #list oluşturduk
s=set(l)  #listeyi set e dönüştürdük.
print(type(s))

x="Ela_lale_elele"
s=set(x)
len(s)

#-------------------------------------------------------------------------------------------

L=["yapay","zeka"]
S=set(L)
S.add("bölümü")                             #set'e kümeye veri ekle
S.remove("yapay")                           #setten kümeden veri çıkar
#Silinecek eleman kümede yoksa remove işleminde hata verir. Hata vermemesi için:
S.discard("yapay")
print(S)
#-------------------------------------------------------------------------------------------

#difference: İki kümenin farkını alır.
set1=set([1,3,5])
set2=set([1,2,3])
x = set1.difference(set2) #set1 de olup set2 de olmayanlar
y = set2.difference(set1) #set2 de olup set1 de olmayanlar
print(x)
print(y)

#-------------------------------------------------------------------------------------------

#set1.intersection(set2)     kesişimini alır
#Birlesim=set1.union(set2)   birleişimini alır

#-------------------------------------------------------------------------------------------

Set1=set([7,8,9])
Set2=set([5,6,7,8,9,10])
#İsdisjoint: İki kümenin kesişimi boş mu?
x = Set1.isdisjoint(Set2)
print(x)

#issubset:alt kümesimidir?
y = Set1.issubset(Set2)
print(y)










