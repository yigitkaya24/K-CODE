from kcode import *

while True:
    a = input("seç: ")
    if  a == "":

        metin = input("Şifrelenmesi için metin giriniz (Boş geçerseniz encode eder, herhangi bir şey yazarsanız decode eder, x yazarsanız programı kapatır): ")

        try:
            sifrelenmis_metin = k_code.encode(metin)
        except:
            sifrelenmis_metin = "ŞİFRELEME YAPARKEN HATA OLUŞTU!"

        print("Şifrelenmiş metin: ", sifrelenmis_metin)

    elif a != "x":

        sifre = input("Çözülmesi için metin giriniz: ")


        cozulmus_metin = k_code.decode(sifre)


        print("Çözülmüş metin: ", cozulmus_metin)

    else:
        break
