class Personeller:
    gunluk_ucret = 50
    personel_listesi = []

    def __init__(self, isim, soyad, gorev, demirbas, calistigi_gunler):
        self.isim = isim
        self.soyad = soyad
        self.gorev = gorev
        self.demirbas = demirbas
        self.calistigi_gunler = calistigi_gunler
        self.personelEkle(isim, soyad, gorev, demirbas, calistigi_gunler)

    def personelEkle(self, isim, soyad, gorev, demirbas, calistigi_gunler):
        self.personel_listesi.append(self.isim)
        self.personel_listesi.append(self.soyad)
        self.personel_listesi.append(self.gorev)
        self.personel_listesi.append(self.demirbas)
        self.personel_listesi.append(self.calistigi_gunler)
    
    def maas(self):
        return self.calistigi_gunler * self.gunluk_ucret
    
    def personelGoruntule(self):
        #print(self.personel_listesi)
        ucret = self.maas()
        return '{} {} {} {} {} {}'.format(self.isim,self.soyad,self.gorev,self.demirbas,self.calistigi_gunler,ucret)
    

        
    
    
personel1 = Personeller("Sinan","İnce","Genelkurmay Başkanı","Darbe","")
personel2 = Personeller("Muharrem","Oğan","Komedyen","Kara Mizah", "")
personel3 = Personeller("Temel","Erdoğan","Reçelci","Vişne Reçeli", "")



print("Personeller listesi aşağıdaki gibidir:")
print(personel1.personelGoruntule())
print(personel2.personelGoruntule())
print(personel3.personelGoruntule())

print(150*"-")

print("Personellerin maaş hesabı için çalıştığı günleri ekleyiniz:")

try:
    personel1 = Personeller("Sinan","İnce","Genelkurmay Başkanı","Darbe",int(input("Sinan'ın çalıştığı günleri gir: ")))
    personel2 = Personeller("Muharrem","Oğan","Komedyen","Kara Mizah",int(input("Muharrem'in çalıştığı günleri gir: ")))
    personel3 = Personeller("Temel","Erdoğan","Reçelci","Vişne Reçeli",int(input("Temel'in çalıştığı günleri gir: ")))

except ValueError as e:
    print("Gün boş girilemez")

print(150*"-")

print("Maaşlar ile personel listesi aşağıdaki gibidir:")
print(personel1.personelGoruntule())
print(personel2.personelGoruntule())
print(personel3.personelGoruntule())