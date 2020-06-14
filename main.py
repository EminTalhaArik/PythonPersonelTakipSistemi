# -*- coding: utf-8 -*-


#Module Importing

import fonksiyonlar

#Variables

devam = True




while devam:
    
    print("*"*32)
    print("1 - Giriş yap")
    print("2 - Kayıt Ol")
    print("0 - Çıkış Yap")
    print("*"*32)

    secim = int(input("Lütfen Bir Seçim Yapınız : "))



#Fonksiyonlara yönlendirme
    if secim == 1:
        fonksiyonlar.girisyap()
        
    elif secim == 2:
        fonksiyonlar.kayitOl()
        
    elif secim == 0:
        
        print("*"*32)
        print("Çıkış Yapılıyor.")
        print("*"*32)
        exit()
    
        
        