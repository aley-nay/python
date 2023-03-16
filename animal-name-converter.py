hayvanlar={
    "kedi":"cat",
    "köpek":"dog",
    "at":"horse",
    "kuş":"bird",
    "papağan":"parrot",
    "kaplumbağa":"turtle",
    "tavşan":"rabbit",
    "aslan":"lion",
    "sincap":"squirrel",
    "su samuru":"sea otter",
    "kanguru":"kangaroo",
    "kısakuyruklu kanguru":"quokka",
    "tilki":"fox",
    "çöl tilkisi":"fennec fox",
    "kapibara":"capybara",
    "gelincik":"mink",
    "keçi":"goat",
    "rakun":"racoon",
    "uçan kuskus":"sugar glider"
}

def cevir(*args, **kwargs):
    for hayvan in args:
        print("{} = {}".format(hayvan,kwargs[hayvan])) 
        

while True:
    kelime=input("hayvan adı gir")
    cevir(kelime, **hayvanlar)