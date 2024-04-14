#                                               SEQUENCE = SIRALAMA
#                                       list,   tuple,  range   kullanılır
#                   list, veriler değiştirilebilir. tuple, veri değişmez. range for döngüsünde kullanılır







#                                                   LIST
#           x=[2,3.0,"Bilgisayar"]
#           print(x[2])                                             print(x[0:2])   ya da print(x[:2])
#
#           çıktı-----------------                                  çıktı-----------------
#           Bilgisayar                                              2 3.0

#           çünkü 0,1,2 diye sayıyor.                               çünkü 0:2 == x<2 kendini değil kendinden öncekini alıyor. 2ye kadar gel, 2yi alma diyoruz. toplarsak 0dan 2ye kadar. 0,1. 2 yok.
#           0->2  1->3.0  2->Bilgisayar                             0.indeks al 1.indeks al 2.indeksi alma

#                                                                   x=['kedi','köpek','kuş','at','yılan','ördek','kaplan']
#                                                                   print(x[-3:-1])
#                                                                   ['yılan', 'ördek']
#                                                                   -ler sağdan sayar. -3 için 0 kaplan 1 ördek 2 yılan. -1 için 0 kaplan. burada -3.indeksten -1.indekse gel ama -1.indeksi alma dedik yukardaki gibi. ondan kaplanı almadı.




#                      LIST                        X                       TUPLE
#           veriler değiştirilebilir                                veriler değiştirilemez
#           x=[2,3.0,"Bilgisayar"]                                  x=[2,3.0,"Bilgisayar"]
#           print(x[2])                                             print(x[2])
#           ---------------------------------------çıktı-----------------------------------
#           Bilgisayar                                              Bilgisayar
#           ---------------------------------------idi-------------------------------------
#           x[2]="Telefon"                                          x[2]="Telefon"
#           print(x[2])                                             print(x[2])
#           ---------------------------------------çıktı-----------------------------------
#           Telefon                                                 HATAHATAHATAHATA
#           veriyi değiştirdik                                      veriyi değiştiremedik





#                                                   RANGE
#                                           range(start,end,step)
#           bir sayıyı başlangıç kabul eder ve istenilen aralıkla döndürür. for'da kullanılır.
#           
#           print(list(range(10)))                                  [0,1,2,3,4,5,6,7,8,9]
#           print(list(range(4,10)))                                [4,5,6,7,8,9]
#           print(list(range(4,10,2)))                              [4,6,8]


#                                   Belki sorularrrrrrrrrr?????????????????
#           1) liste oluştur
#           arabalar = ['Bmw','Mercedes','Opel','Mazda']

#           2) kaç elemanlı
#           result = len(arabalar)  # result = 4

#           3) ilk ve son eleman
#           result = arabalar[0]    #ilk
#           result = arabalar[3]    #son
#           result = arabalar[-1] # tersten -1. indeks en son elemana karşılık gelir.

#           4) mazayı toyota yap
#           arabalar[-1]="toyota"   #-1 demek son eleman demek. -ler hep sondan okunduğu için -lerde ise baştaki eleman oluyor.

#          5) -2 değeri ne
#          result = arabalar[-2]
#          print(result)            #mercedes           -1 olsa mazda yazdıracaktı


#          6) listenin ilk 3 eleman
#          result = arabalar[0:3]
#          result = arabalar[:3]
#          result = arabalar[-1:]   #-1 mazda idi mazdayı saymadan ilk üçü aldı

#           5) Mercedes listenin bir elemanı mıdır ?
#          result = 'Mercedes' in arabalar
#          print(result) # True