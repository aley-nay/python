#                                               SET = VERİ TİPİ
#                                           sıralamayla karıştırma.
#                               sıralama (dictionary) [] ile, set {} ile.
#                                   sıralamada indeks var, sette yok. print(kume[2]) desen hata verir


#                                                   SET


#                               kume={"ali", "ayşe", "veli", "ayşe", 2, 3.0}

#                               add                 kume.add("levent")                  leventi ekledi
#                               clear               kume.clear()                        kümeyi sildi
#                               copy                kume_yedek=kume.copy()              kümeyi yedekledi
#                               update              kume_2={"ece", "murat", "derya"}
#                                                   kume.update(kume_2)                 yeniler. eskiye yeniyi ekler
#                               remove              kume.remove("ali")                  siler   (dizide olmayan bir şeyi silmeye kalkınca hata verir)
#                               discard             kume.discard("ali")                 siler   (hata vermez)
#                               pop                 kume.pop()                          ilk elemanı siler
#                               union               print(kume_A.union(kume_B))         2 kümeyi birleştirir
#                               intersection        print(kume_A.intersection(kume_C))  2 küme kesişimi verir
#                               intersection_update kume_A.intersection_update(kume_C)  kesişim ve update yapar
#                               isdisjoint          print(kume_A.isdisjoint(kume_B))    kesişim boş mu dolu mu kontrol yapıp true false döndürür
#                               difference          print(kume_A.difference(kume_B))    birleşim dışında kalanlar
#                               difference_update   kume_A.difference_update(kume_B)        "       "       "ı updateler
#                               issubset            kume_D.issubset(kume_C)             bir kümenin başka bir kümenin alt kümesi olup olmadığını kontrol eder. true false
#                               Issuperset          kume_D.issubset(kume_C)             yukardakinin zıttı. üst küme olup olmadığını soruyor. true false



#                                                   FORZENSET
#                               ekle silme güncelleme vs yapılamaz
#                               a=frozenset(["ali","ayşe","veli", 2, 3.5])
