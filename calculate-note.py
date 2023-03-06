print("ortalama hesabı programı")
vize=int(input("vize notu gir"))
final=int(input("final notu gir"))
if len(str(vize))<=0:
    print("hata: vize notu boş bırakılamaz")
else:
    #print("vize:",vize)
    #print("final:",final)
    #ortalama = print("ortalama:", vize%40, "+", final%60, "=", vize + final)
    ort1=(vize*0.4)+(final*0.6)
    print("ortalaman:",ort1)
    if(ort1<60):
        print("kaldın. bütünlemeye girecek misin")
        kaldi=str(input("E,H"))
        if(kaldi.upper()=="E"):
            print("e seçti")
            but=int(input("büt notu gir"))
            #print(but)
            ort2=(vize*0.4)+(but*0.6)
            print("ortalaman:",ort2)
            if(ort2<60):
                print("kaldın. artık seneye")
            else:
                print("geçtin")
        else:
            print("h seçti. kaldı")
    else:
        print("geçtin")