
#           APPEND
# liste sonuna 1 eleman ekler

liste = ["cemre","cansu","ceylin"]
liste.append("mercan")
print(liste)


#           REMOVE
# kaldırır
liste = ["cemre","cansu","ceylin","mercan"]
liste.remove("mercan")
print(liste)


#           INSERT:EKLE                                          DİKKAT:  liste.insert(0,"cem") ve liste[0] = cem farklı
# indis değeriyle eleman ekler
liste = ["cemre","cansu","ceylin"]
liste.insert(0,"cem")   #listeyi bozmadı. 0.indise cem yazdı. cemre'nin indisi 1 oldu.
#liste[0] = "cem"       0.indiste cemre vardı, cem oldu
print(liste)

liste = ["cemre","cansu","ceylin"]
liste.insert(len(liste),"hasan")    #listenin sonuna hasan ekledi
print(liste)



#            EKLE : APPEND, INSERT
liste = ["cemre","cansu","ceylin"]
liste.append("mercan")
liste.insert(0,"ayşe")
liste[1] = "derya"
print(liste)


#           POP:SİL                                                 DİKKAT:   liste.remove(cemre)  ve liste.pop(0)
liste = ["cemre","cansu","ceylin"]
liste.pop(0)                        #0.indis cansu sildi
print(liste)



#           SİL : POP, REMOVE, del
liste = ["cemre","cansu","ceylin","seyran","şırdan"]
liste.pop(0)
liste.remove("şırdan")
del (liste[2])  
print(liste)





#           COUNT:KAÇ ADET SAYAR
liste = ["cemre","cansu","ceylin"]
print(liste.count("cemre"))         #1 tane cansu var dedi

#           COPY:LİSTE KOPYALA-YEDEKLE
liste = ["cemre","cansu","ceylin"]
liste_yedek = liste.copy()
print(liste_yedek)


#           EXTENDS:İKİ LİSTE BİRLEŞTİRME
kizlar = ["cemre","cansu","ceylin"]
erkekler = ["taro", "emir", "tekin"]
kizlar.extend(erkekler)
print(kizlar)

