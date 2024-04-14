degisken = "kedi"

#karakter uzunluğu
print(len(degisken))

#büyük yap
print(degisken.upper())

#küçük yap
print(degisken.lower())

#büyük mü diye soruyor, true false dönüyor
print(degisken.isupper())

#küçük mü diye soruyor, true false dönüyor
print(degisken.islower())

#kediyi köpek yapar
print(degisken.replace("kedi","köpek"))

#boşlukları siler
degisken = "    kedi   "
print(degisken.strip())

#ayırır, liste olarak
degisken = "kedi köpek kuş"
print(degisken.split())


#böler substring
degisken = "köpek"
print(degisken[0:3])

#türünü tipini verir
print(type(degisken))


print("uzaya","git", sep="**")
#uzaya**git


print("10"+2)
#type error

print("gelecek_geldi".replace("i","ı"))
print("_kedi_".strip("_"))

degisken="1012340"
degisken = degisken+"1"
print(degisken.strip("1"))