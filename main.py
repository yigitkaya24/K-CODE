from kcode import *

metin = input("Şifrelenmesi için metin giriniz: ")

try:
    sifrelenmis_metin = k_code.encode(metin)
except:
    sifrelenmis_metin = "ŞİFRELEME YAPARKEN HATA OLUŞTU!"

print("Şifrelenmiş metin: ", sifrelenmis_metin)

sifre = input("Şifrelenmesi için metin giriniz: ")


cozulmus_metin = k_code.decode(sifre)


print("Çözülmüş metin: ", cozulmus_metin)

input()