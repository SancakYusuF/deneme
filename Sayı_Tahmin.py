'''
  1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile 
  buldurmaya çalışın
  ** "radom modülü" kullan
  ** 100 üzerinden puanlama yapın. her soru 20 puan
  ** hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
  üzerinden hesaplansın
'''
import random
sayi = random.randint(1,100)
hak = 6

while hak > 0:
    hak -= 1
    tahmin = int(input('Tahmininiz Nedir: '))

    if sayi == tahmin:
        print('Tebrikler Bildiniz')
        break
    elif sayi > tahmin:
        print(f'Yukarı, Kalan Hak: {hak}')
    else:
        print(f'Aşağı, Kalan Hak: {hak}')

    if hak == 0:
        print(f'Hakkınız Bitii :/. Tutulan Sayı: {sayi}')