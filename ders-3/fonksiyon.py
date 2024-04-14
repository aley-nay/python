#Kullanıcını girdiği sayıya kadar olan çift sayıları ekrana yazdıran kod
sayi=int(input("sayiyi girin:"))

for i in range(0,sayi):
    if (i%2==0):
        print(i)




#Girilen bir sayının faktöriyelini hesaplayan kod
sayi=int(input("sayiyi girin:"))

fakt=1

for i in range(2,sayi+1):
    fakt=fakt*i
print("Girilen sayinin faktoriyeli:",fakt)

#Hesap Makinesi
sayi1=int(input("birinci sayiyi girin:"))
sayi2=int(input("ikinci sayiyi girin:"))

print("toplama icin +,cikarma icin -, carpma icin * bolme icin / yazınız:")

secim=input("secim yapınız:")

if (secim=='+'):
    print("toplam:",sayi1+sayi2)
elif (secim=='-'):
    print("fark:",sayi1-sayi2)
elif (secim=='*'):
    print("carpim:",sayi1*sayi2)
elif (secim=='/'):
    print("bolum:",sayi1/sayi2)
else:
    print("yanlis secim yaptiniz")

#Pozitif-Negatif
sayi=int(input("Bir sayi giriniz:"))

if sayi<0:
    print("Girilen sayi negatiftir")
elif sayi>0:
    print("Girilen sayi pozitiftir.")
else:
    print("Girilen sayi sifirdir.")


#asal sayı
sayac=0
sayi=input("sayi giriniz:")

for i in range(2,int(sayi)):
    if(int(sayi)%i==0):
        sayac+=1
        break
if (sayac!=0):
    print(sayi +" degeri asal degildir.")
else:
    print(sayi +" degeri asaldir.")


#--------------------------------------------------------------------

maaslar=[10000,20000,15000,25000]

#maaşlara %20 zam yaptıktan sonra oluşacak yeni değerler

def guncel_maas(x):
    print(x*0.2+x)
        
guncel_maas(100)

for i in maaslar:
    guncel_maas(i)

#---------------------------------

#maaşı 20000 den fazla olanlara %10, 20000 den az olanlara %20 zam yapalım

def maas_ust(x):
    print(x*0.1+x)
    
def maas_alt(x):
    print(x*0.2+x)
    
for i in maaslar:
    if i>=20000:
        maas_ust(i)
    else:
        maas_alt(i)
        
        
def yuksek(i):
    print(i*0.1+i)

def dusuk(i):
    print(i*0.2+i)
        
maaslar=[10000,20000,15000,25000]
for i in maaslar:
    if i>20000:
        yuksek(i)
    else:
        yuksek(i)
        
        
        

#----------------------------
ogrenci=["ali","veli","isik","berk"]
for i in ogrenci:
    print(i)

sayi=1
while sayi<10:
        sayi+=1
        print(sayi)
        
        
