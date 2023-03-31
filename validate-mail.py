while True:
    mail=str(input("mail gir"))

    #bosluk ara
    bosluk = ' ' in mail

    #com @ var mı
    dom = ("@gmail.com","@hotmail.com")
    varmi = mail.endswith(dom)


    #sembol var mı kontrol
    sembol0 = mail.strip("@gmail.moc")
    sembol1 = sembol0.isalnum()
    
    
    #türkçe var mı kontrol
    tr = "ğüşıöçĞÜŞİÖÇ"
    en = "gusiocgusioc"
    cevir0 = mail.maketrans(tr,en)
    cevir1 = mail.translate(cevir0)
    
    #küçük karakter
    kucult0 = cevir1.lower()
    #kucult1= kucult0.islower()



    if(bosluk == True):                 #boşluk varrrrsaaaaaaaa  =>         boşluk                                  kontrol
        print("boşluk kullanma")

    elif(varmi == False):               #domain yoksaaaa        =>          domain (@gmail.com, @hotmail.com)       kontrol
        print("domain yok")
    
    elif(sembol1==False):               #sembol yoksaaaaaaa      =>         sembol (^+_-%/=*?'")                    kontrol
        print("sembol kullanma")

    elif(cevir1 != " "):                #türkçe vaaaaaarsaa     =>          türkçe (ğüşıöçĞÜŞİÖÇ)                   kontrol       
        print(kucult0)                  #büyük varrrrsaaaaaaa   =>          büyük (ABCDE)                           kontrol

    else:
        print("hata")                  
