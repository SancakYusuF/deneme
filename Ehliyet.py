#     Kullanıcıdan isim, yaş ve egitim bilgilerini isteyip ehkiyet alabilme durumunu kontrol ediniz
#     Yaş en az 18 
#     Eğitim dumunu en az lise 

name   = input('İsminiz: ')
age    = int(input('Yasınız: '))
egitim = input('Egitim Durumunuz(ilkokul, ortaokul, lise, üniversite): ')


if (age >= 18):
    if (egitim == 'lise' or egitim == 'üniversite'):
        print('Ehliyet alabilirsiniz')  
    else:
        print('Ehliyet Alamazsınız. Eğitim durumunuz yetersiz' )

else:
    print('Ehliyet Alamazsınız. Yaşınız Yetersiz')
