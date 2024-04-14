pi = 3.14
r = input("yarı çap gir") #string alır, işleme girmez
r = float(input("yarı çap gir")) #işleme girer
alan = pi * (r ** 2)
cevre = 2 * pi * r

print("alan",alan)
print("çevre",cevre)





r = float(input("yarı çap gir"))
alan = pi * (r ** 2)
print(type(alan))
cevre = 2 * pi * r
print(type(cevre))

#print("alan:"+alan+"çevre"+cevre) #bu sadece string birleştirmede olur int float da çalışmaz
print("alan:"+ str(alan)+"çevre"+ str(cevre))
