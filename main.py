from kcode import *

metin = input("Şifrelenmesi için metin giriniz: ")

try:
    sifrelenmis_metin = k_code.encode(metin)
except:
    sifrelenmis_metin = "ŞİFRELEME YAPARKEN HATA OLUŞTU!"

print("Şifrelenmiş metin: ", sifrelenmis_metin)

metin = input("Şifrelenmesi için metin giriniz: ")

try:
    sifrelenmis_metin = k_code.encode(metin)
except:
    sifrelenmis_metin = "ŞİFRELEME YAPARKEN HATA OLUŞTU!"

print("Şifrelenmiş metin: ", sifrelenmis_metin)