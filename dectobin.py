




def turn(decX):                         #dec diye yollamıştım, decX olarak aldım
    
    if(decX==0):                        #boş mu dolu mu diye kontrol ettim
        return
    else:
        turn(int(decX/2))               #fonksiyonumu çağırdım. bu fonksiyon rekürsif bir fonksiyon çünkü kendi kendini çağıracak. birazdan anlatıcam
                                        #örn 9 sayısı
                                        #9/2    kalan 1 elde 4
                                        #4/2    kalan 0 elde 1
                                        #1/2...................diye gidiyor ta ki kalan 0 olana dek


        print(decX%2, end="")           #kalanı tutuyor
                                        #4 ile başa dönüyor
                                        #kalanı tutuyor
                                        #1 ile başa dönüyor




dec = int(input("dec:"))                #kullanıcıdan veriyi alıp dec adlı değişkene attım
turn(dec)                               #fonksiyonun içine yolladım



print('\n{0:b}'.format(dec))
"""
b = binary, 2lik
o = octal, 8lik
x = hexadecimal, 16lık
diye çeviriyor
"""


print('\n:'+bin(dec)[2:])
"""
bin() = binary
hex() = hexadecimal
diye çeviriyor
"""