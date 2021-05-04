#    Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız
#    1.Bakım => 1.Yıl
#    2.Bakım => 2.Yıl
#    3.Bakım => 3.Yıl 
#    **Süre hesabını alınan gün, ay, yıl bigisine göre gün bazlı hesaplayınız
#    *** datetime modülünü kullanmanız gerekiyor

days = int(input('Araç kaç gündür tafikte: '))

if days > 0 and days <= 365:
    print('1.Servis Aralığı')
elif days > 365 and days <= 365*2:
    print('2.Servis Aralığı')
elif days > 365*2 and days <= 365*3:
    print('3.Servis Aralığı')
else:
    print('Hatalı Gün Bilgisi Girdiniz')    





