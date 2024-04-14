def kare_al(x):
    sonuc = x**2
    return sonuc

sayi = int(input("sayı gir"))
sonuc = kare_al(sayi)

print(sonuc)
#-----------------------------------
def carpma(x,y):
    print(x*y)
    
carpma(y=2,x=4) 
#------------------------------------
def hesap(yol, zaman):
    hiz = yol / zaman
    return hiz

# Fonksiyonu çağırma
sonuc = hesap(100, 5)

# Sonucu ekrana yazdırma
print(sonuc)
#----------------------------------
def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj
    
cikti=direk_hesap(25, 40, 70)*5
print(cikti)
#--------------------------------------
def eleman_ekle(ana_liste, yeni_eleman):
    ana_liste.append(yeni_eleman)
    return ana_liste

x = []
eleman_ekle(x, 1)  # Fonksiyon aracılığıyla listeye bir eleman eklendi

# Listeyi yazdırma
print(x)
#-----------------------------------------

gelir=500
gider=300
if gelir>gider:
    print("gelir giderden buyuk")
    print(gelir*2)
else:
    print("Gider gelirden buyuk")
