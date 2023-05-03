import random                               #rastgele sayı getirmek için random kütüphanesi

sıra = 4                                    #4x4lük matris olacağı için 4'e 4 sınır
sutun = 4                                   #4x4lük matris olacağı için 4'e 4 sınır
matris1 = []                                #boş liste, doldurulacak
matris2 = []                                #boş liste, doldurulacak

for i in range(sıra):                       #sıra = 4, 4'e kadar götür
    temp = []                               #temp = temporary, boş liste
    for j in range(sutun):                  #sutun = 4, 4'e kadar götür
        değer = random.randint(0,9)         #0'dan 9'a rastgele sayı
        temp.append(değer)                  #tempte değer = rastgele sayı tuttum
    matris1.append(temp)                    #tempi matris1'e aktardım
for i in range(sıra):                       #"
    temp = []                               #"
    for j in range(sutun):                  #"
        değer = random.randint(0,9)         #"
        temp.append(değer)                  #"
    matris2.append(temp)                    #"
    
print("1. matris",matris1)
print("2. matris",matris2)

#2 matrisin toplamı:

det=[ [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
for i in range(len(matris1)):                               #i matrisin sınırına kadar aldım
    for j in range(len(matris2)):                           #j matrisin sınırına kadar aldım
        det[i][j] = matris1[i][j] + matris2[i][j]           #2 matrisi topladım
print("matrislerin toplamı: ",det)


#determinantı
determinant = det[0][0] * det[1][1] * det[2][2] * det[3][3] - det[0][0] * det[1][1] * det[2][3] * det[3][2] - det[0][0] * det[1][2] * det[2][1] * det[3][3] + det[0][0] * det[1][2] * det[2][3] * det[3][1] + det[0][0] * det[1][3] * det[2][1] * det[3][2] - det[0][0] * det[1][3] * det[2][2] * det[3][1] - det[0][1] * det[1][0] * det[2][2] * det[3][3] + det[0][1] * det[1][0] * det[2][3] * det[3][2] + det[0][1] * det[1][2] * det[2][0] * det[3][3] - det[0][1] * det[1][2] * det[2][3] * det[3][0] - det[0][1] * det[1][3] * det[2][0] * det[3][2] + det[0][1] * det[1][3] * det[2][2] * det[3][0] + det[0][2] * det[1][0] * det[2][1] * det[3][3] - det[0][2] * det[1][0] * det[2][3] * det[3][1] - det[0][2] * det[1][1] * det[2][0] * det[3][3] + det[0][2] * det[1][1] * det[2][3] * det[3][0] + det[0][2] * det[1][3] * det[2][0] * det[3][1] - det[0][2] * det[1][3] * det[2][1] * det[3][0] - det[0][3] * det[1][0] * det[2][1] * det[3][2] + det[0][3] * det[1][0] * det[2][2] * det[3][1] + det[0][3] * det[1][1] * det[2][0] * det[3][2] - det[0][3] * det[1][1] * det[2][2] * det[3][0] - det[0][3] * det[1][2] * det[2][0] * det[3][1] + det[0][3] * det[1][2] * det[2][1] * det[3][0]
print("Toplanan 2 matrisin determinantı: ",determinant)