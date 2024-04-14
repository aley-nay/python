website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#uzunluk
print(len(course))

#www al
print(website[7:10])

#com al
print(website[22:25])

#courseun ilk 15 ve son 15 al
print(course[:15])
print(course[15:])

#courseu tersten yaz
print(course[::-1])

name, surname, age, job = "tufancan","demirkılıç",19,"mühendis"
result = "benim adım {0}{1}, yaşım{2} ve mesleğim {3}".format(name,surname,age,job)