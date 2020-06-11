# -*- coding: utf-8 -*-

import sqlite3

def kullaniciSistemAcilsin(kullaniciAdi,sifre):
    print("Personel Sistemi Açıldı.")
    
    devam = True
    
    while devam:
        print("======================")
    
        print("1 - Bilgilerimi Görüntüle")
        print("2 - Kullanıcı Adı Değiştir")
        print("3 - Şifre Değiştir")
        print("0 - Çıkış Yap")
        
        secim = int(input("Lütfen Bir İşlem Seçiniz : "))
        
        if secim == 1:
            bilgileriGoruntule(kullaniciAdi,sifre)
            
        elif secim == 2:
            kullaniciAdiDegistir(kullaniciAdi,sifre)
            
        elif secim == 3:
            sifreDegistir(sifre,kullaniciAdi)

        elif secim == 0:
            devam = False
            
            
def personelGoster():
    connection = sqlite3.connect("kullanicilar.db")
    
    imlec = connection.cursor()
    
    imlec.execute("SELECT no,isim,soyisim,kullaniciAdi FROM kullanicilar")
    
    data = imlec.fetchall()
    print("***************************")
    for i in data:
        print("Numara = " + str(i[0]))
        print("İsim = " + i[1])
        print("Soyisim = " + i[2])
        print("Kullanıcı Adı = " + i[3])
        print("***************************")
        
    connection.close()
    
    
def yetkilendir():
    
    print("Yetkilendirme sistemi Açıldı.")
    
    connection = sqlite3.connect("kullanicilar.db")
    
    imlec = connection.cursor()
    
    print("Kullanıcıları Görmek İstermisiniz ? ")
    
    
    numara = input("Lütfen yetki vermek istediğiniz personelin numarasını giriniz : ")
    
    print("1 - Yönetici  2 - kullanıcı")
    yetki = int(input("Personele verilecek yetkiyi girin : "))
        
    verilecekYetki = "kullanici"
        
    if yetki == 1:
        verilecekYetki = "admin"
    else:
        verilecekYetki = "kullanici"
    
    
    imlec.execute("UPDATE kullanicilar set yetki = ? WHERE no= ?",
                  (verilecekYetki,numara))
   
    connection.commit()
    
    print("Yetki Başarıyla Belirlendi")
    
    
    connection.close()
    
    
def bilgileriGoruntule(kullaniciAdi,sifre):
    
    connection = sqlite3.connect("kullanicilar.db")
    
    imlec = connection.cursor()
    
    imlec.execute("SELECT * FROM kullanicilar WHERE kullaniciAdi = ? AND sifre = ?",
                  (kullaniciAdi,sifre))
    
    data = imlec.fetchall()
    
    for i in data:
        print("===============")
        print("İsminiz : " + i[0])
        print("Soyisim : " + i[1])
        print("Kullanıcı Adınız : " + i[2])
        print("Şifreniz : " + i[3])
        print("Numaranız : " + str(i[5]))
        print("===============")
        
    connection.close()
    
    print("Bİlgileriniz Başarıyla Görüntülendi.")
    
def kullaniciEkle():
    connection = sqlite3.connect("kullanicilar.db")
    
    imlec = connection.cursor()
    
    isimGiris = input("Lütfen Personel İsmini Giriniz : ")
    soyisimGiris = input("Lütfen Personel Soyismini Giriniz : ")
    kullaniciAdiGiris = input("Lütfen Personelin Kullanıcı Adını Giriniz : ")
    sifreGiris = input("Lütfen Personel Şifresini Gİriniz : ")
    
    
    
    imlec.execute("INSERT INTO kullanicilar(isim,soyisim,kullaniciAdi,sifre) VALUES (?,?,?,?)",
                  (isimGiris,soyisimGiris,kullaniciAdiGiris,sifreGiris))
   
    connection.commit()
    
    print("Personel Başarıyla Oluşturuldu.")
    
    connection.close()
   
    
def kullaniciKaldir():
    try:
        connection = sqlite3.connect("kullanicilar.db")
        
        imlec = connection.cursor()
        
        numaraGiris = input("Lütfen Silmek İstediğiniz Personelin Numarasınız Giriniz : ")
        
        imlec.execute("DELETE FROM kullanicilar WHERE no = ?",
                      (numaraGiris))
    
        connection.commit()
        
        print("Kullanıcı Başarıyla Kaldırıldı.")
        
    except sqlite3.Error as error:
        print("Kullanıcı Şu Hatadan Dolayı Silinemedi = " ,error)
        
    finally:
        if connection:
            connection.close()
            
       
def kullaniciAdiDegistir(kullaniciAdi, sifre):
    print("Kullanıcı Adı Değiştirme Sistemi Açıldı.")
    
    connection = sqlite3.connect("kullanicilar.db")
    
    imlec = connection.cursor()
    
    kullaniciAdi = kullaniciAdi
    yeniKullaniciAdiniz = input("Lütfen Yeni Kullanıcı Adınızı Giriniz : ") 
    
    imlec.execute("UPDATE kullanicilar SET kullaniciAdi = ? WHERE kullaniciAdi = ? AND sifre = ?",
                  (yeniKullaniciAdiniz,kullaniciAdi,sifre))

    connection.commit()
    print("=======================")
    
    print("Kullanıcı Adı Başarıyla Değiştirildi.")

    print("=======================")
    
    connection.close()    
    
    girisyap()
    
def sifreDegistir(sifre,kullaniciAdi):
    connection = sqlite3.connect("kullanicilar.db")
    imlec = connection.cursor()
    
    
    yeniSifreniz = input("Yeni Şifrenizi Giriniz : ")
    
    imlec.execute("UPDATE kullanicilar SET sifre = ? WHERE sifre = ? AND kullaniciAdi = ? ",
                  (yeniSifreniz,sifre,kullaniciAdi))
    
    connection.commit()
    print("=======================")
    print("Şifreniz Başarıyla Değiştirilmiştir.")
    print("Şifrenizi Tekrar Değiştirmek İçin Tekrar Giriş Yapın.")
    print("=======================")
    connection.close()
    
    girisyap()
    
def adminSistemAcilsin(kullaniciAdi,sifre):

    kullaniciAdi = kullaniciAdi
    sifre = sifre
    
    devam = True
    print("*"*32)
    print("Sistem Açıldı.")
    print("*"*32)
    
    while devam:
        print("=======================")
        print("1 - Personelleri Göster")
        print("2 - Yetkilendir")
        print("3 - Personel Ekle/ Kaldır")
        print("4 - Kullanıcı Adı Değiştir")
        print("5 - Şifre Değiştir")
        print("6 - Bilgilerimi Görüntüle")
        print("0 - Çıkış Yap")
        
        secim = int(input("Lütfen Bir Seçim Yapınız : "))
        
        if secim == 1:
            personelGoster()
        
        elif secim == 2:
            yetkilendir()
            
        elif secim == 3:
            print("1 - Personel Ekle")
            print("2 - Personel Kaldır")
            
            secim2 = int(input("Lütfen Yapıcağınız İşlemin  Numarasını Giriniz :"))
            
            if secim2 == 1:
                kullaniciEkle()
                
            elif secim2 == 2:
                kullaniciKaldir()
                
            else:
                print("Yanlış Seçim Yapıldı.")
            
        elif secim == 4:
            kullaniciAdiDegistir(kullaniciAdi,sifre)
            
            
        elif secim == 5:
            sifreDegistir(sifre,kullaniciAdi)
        
        elif secim == 6:
            bilgileriGoruntule(kullaniciAdi,sifre)
            
        
        elif secim == 0:
            devam = False
            
    print("=======================")
    
    
def adminKontrol(imlec,kullaniciAdiGiris,sifreGiris,default):
    
    imlec.execute("SELECT kullaniciAdi,sifre FROM kullanicilar WHERE kullaniciAdi = ? AND sifre = ? AND yetki = ?" ,
                  (kullaniciAdiGiris,sifreGiris,default))

    data = imlec.fetchone()
        
    if data:
        
        kullaniciAdi = kullaniciAdiGiris
        sifre = sifreGiris
        
        adminSistemAcilsin(kullaniciAdi,sifre) 
        
    else:
        kayitOlmakİstermisiniz()
        
    

def kullaniciKontrol(imlec,kullaniciAdiGiris,sifreGiris,default2):
    imlec.execute("SELECT kullaniciAdi,sifre FROM kullanicilar WHERE kullaniciAdi = ? AND sifre = ? AND yetki = ?" ,
                  (kullaniciAdiGiris,sifreGiris,default2))
    
    data = imlec.fetchone()
        
    if data:
        kullaniciAdi = kullaniciAdiGiris
        sifre = sifreGiris
        
        kullaniciSistemAcilsin(kullaniciAdi,sifre)        
    else:
        kayitOlmakİstermisiniz()
        
    

def kayitOlmakİstermisiniz():
    
    print("Hesabınız Bulunamadı. Kayıt Olmak İçin -1- Çıkış Yapmak İçin -0- ")
    secim = int(input("Kayıt Olmak İstermisinz : "))
    
    if secim == 1:
        kayitOl()
        
    elif secim == 0:
        print("Anasayfaya Yönlendiriliyor..")
        

def girisyap():  #Sisteme Gİriş Alanı
    
    default = "admin"
    default2 = "kullanici"
    
    connection = sqlite3.connect("kullanicilar.db")

    imlec = connection.cursor()
    
    imlec.execute("CREATE TABLE IF NOT EXISTS kullanicilar (isim,soyisim,kullaniciAdi,sifre,yetki)")
    
    connection.commit()

    print("Giriş Sistemi Açıldı.")

    kullaniciAdiGiris = input("Lütfen Kullanıcı Adı Giriniz : ")
    sifreGiris = input("Lütfen Şifre Gİriniz : ")
    
    print("1 - Yönetici 2 - Personel")
    
    yetkiGiris = int(input("Lütfen yetkinizi Belirtiniz : "))
    
    if yetkiGiris == 1:
        adminKontrol(imlec, kullaniciAdiGiris, sifreGiris, default)
            
    elif yetkiGiris == 2:
        kullaniciKontrol(imlec, kullaniciAdiGiris, sifreGiris,default2)
        
    connection.close()
        
              
def kayitOl():  #Kayıt Alanı
    
    default = "kullanici"
    
    connection = sqlite3.connect("kullanicilar.db")
    imlec = connection.cursor()
    
    imlec.execute("CREATE TABLE IF NOT EXISTS kullanicilar (isim,soyisim,kullaniciAdi,sifre,yetki)") 
    
    connection.commit()
    
    isimKayit = input("Lütfen İsminizi Giriniz : ")
    soyisimKayit = input("Lütfen Soyisminizi Giriniz : ")
    
    kullaniciAdikayit = input("Lütfen Kullanıcı Adınızı Giriniz : ")
    sifreKayit = input("Lütfen Şifrenizi Giriniz : ")
    
    imlec.execute("INSERT INTO kullanicilar(isim,soyisim,kullaniciAdi,sifre,yetki) VALUES (?,?,?,?,?)",
                  (isimKayit,soyisimKayit,kullaniciAdikayit,sifreKayit,default))
    
    connection.commit()
    
    print("Başarılı Bİr Şekilde Kayıt Oldun. \n Şimdi Giriş yapabilirsin.")
    
    connection.close()
    
    
    