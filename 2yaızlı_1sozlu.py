#       Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre not aralıgına karsılık 
#       gelen sayıyı yazdırınız
#       0 -24  => 0 
#       25-44  => 1
#       45-54  => 2
#       55-69  => 3
#       70-84  => 4
#       85-100 => 5

yaızılı1 = int(input('1.Yazılı Notunuzu Giriniz: '))
yaızılı2 = int(input('2.Yazılı Notunuzu Giriniz: '))
sözlü    = int(input('Sözlü Notunuzu Giriniz: '))


ortalama = (yaızılı1 + yaızılı2 + sözlü) / 3

# notlar 0dan küçük 100 den büyük olamaz şeklinde ayar yapılması gerek ben yapmadım :D






if ortalama < 25 and ortalama >= 0:
    print('Notunuz 0'),
elif ortalama < 45 and ortalama >= 25:
    print('Notunuz 1')
elif ortalama < 55 and ortalama >= 45:     
    print('Notunuz 2')
elif ortalama < 70 and ortalama >= 55:
    print('Notunuz 3')
elif ortalama < 85 and ortalama >= 70:
    print('Notunuz 4')
elif ortalama <= 100 and ortalama >= 85:
    print('Notunuz 5') 
# else olamsada oluyor garip bunu sor
#else:
#   print('Yanlış bilgi girdiniz')
    
print(f'Ortalamanız {ortalama}')

if ortalama > 60 :
    print('Sınavı Geçtiniz')

