# K-CODE Kullanım Kılavuzu (User Guide)

---

# Türkçe ( Turkish 🇹🇷 )

### Kütüphaneyi python projenize dahil etmek için aşağıdaki adımları uygulayın

1. Kütüphaneyi [buraya](https://github.com/yigitkaya24/K-CODE/releases) tıklayarak indirin (.py uzantılı olan dosyayı)
    
    ![Untitled](K-CODE%20Kullan%C4%B1m%20K%C4%B1lavuzu%20(User%20Guide)%206f84edef25964a43abc513ac9e1c1429/Untitled.png)
    
2. İndirdiğiniz dosyayı projenizinle aynı klasöre koyun ve bir alt klasöre yerleştirmeyin
    
    ![Untitled](K-CODE%20Kullan%C4%B1m%20K%C4%B1lavuzu%20(User%20Guide)%206f84edef25964a43abc513ac9e1c1429/Untitled%201.png)
    
3. Python projenize eklemek için projenizin başına aşağıdaki kodu ekleyin
    
    ```python
    from kcode import *
    ```
    

### Komutların kullanımı aşağıdaki gibidir

`k_code.encode(”Şifreleyeceğiniz metin”)` ⇒ Girdiğiniz metni K-CODE şifreleme metoduna göre şifreler

`k_code.decode(”Şifrelenmiş metin”)` ⇒ Girdiğiniz şifreyi K-CODE şifreleme metoduna göre çözer

`base8.encode(”base8 ile şifrelenecek metin”)` ⇒ Girdiğiniz metni K-CODE şifreleme metodu için geliştirilmiş base8 şifreleme metoduyla şifreler

`base8.encode(”base8 ile şifrelenmiş metin”)` ⇒ Girdiğiniz şifreyi K-CODE şifreleme metodu için geliştirilmiş base8 şifreleme metoduyla çözer

`matris2D.encode(”matris2D ile şifrelenecek metin”)` ⇒ Girdiğiniz metni K-CODE şifreleme metodu için geliştirilmiş yalnızca base8 kodlarını şifreleyebilen 2 boyutlu matris yansıması ile şifreler

`matris2D.encode(”matris2D ile şifrelenmiş metin”)` ⇒ Girdiğiniz şifreyi K-CODE şifreleme metodu için geliştirilmiş yalnızca base8 kodlarını şifreleyebilen 2 boyutlu matris yansıması ile çözer

- NOT: Yalnızca ASCII karakterlerini desteklemektedir, harici karakter kullanıldığı takdirde hatalı şifreleme olur
- NOT: Komutları kullanırken `try` bloğu içine yazmanız hata algılandığında programınızın çökmesini engeller (Tavsiye Edilir)
    
    ```python
    from kcode import *
    
    metin = input("Şifrelenmesi için metin giriniz: ")
    
    try:
        sifrelenmis_metin = k_code.encode(metin)
    except:
        sifrelenmis_metin = "ŞİFRELEME YAPARKEN HATA OLUŞTU!"
    
    print("Şifrelenmiş metin: ", sifrelenmis_metin)
    ```
    

# English ( İngilizce 🇬🇧 )

### Follow the steps below to include the library in your python project

1. Download the library by clicking [here](https://github.com/yigitkaya24/K-CODE/releases) (file with .py extension)
    
    ![Untitled](K-CODE%20Kullan%C4%B1m%20K%C4%B1lavuzu%20(User%20Guide)%206f84edef25964a43abc513ac9e1c1429/Untitled.png)
    
2. Put the downloaded file in the same folder as your project and do not place it in a subfolder
    
    ![Untitled](K-CODE%20Kullan%C4%B1m%20K%C4%B1lavuzu%20(User%20Guide)%206f84edef25964a43abc513ac9e1c1429/Untitled%201.png)
    
3. Add the following code at the beginning of your project to add it to your Python project
    
    ```python
    from kcode import *
    ```
    

### Usage of commands is as follows

`k_code.encode(”The text you will encrypt”)` ⇒ Encrypts the text you enter according to the K-CODE encryption method

`k_code.decode(”Encrypted text”)` ⇒ Decrypts the password you entered according to the K-CODE encryption method

`base8.encode(”Text to be encrypted with base8”)` ⇒ Encrypts the text you enter with the base8 encryption method developed for the K-CODE encryption method

`base8.encode(”Text encrypted with base8”)` ⇒ Decrypts the password you entered with the base8 encryption method developed for the K-CODE encryption method

`matris2D.encode(”Text to be encrypted with matrix2D”)` ⇒ Encrypts the text you enter with a 2D matrix reflection developed for the K-CODE encryption method, which can only encode base8 codes

`matris2D.encode(”Text encrypted with matrix2D”)` ⇒ Decrypts the password you enter with a 2D matrix reflection developed for the K-CODE encryption method, which can only encode base8 codes

- NOTE: It only supports ASCII characters, incorrect encryption will occur if external characters are used
- NOTE: When using commands, typing in a `try` block will prevent your program from crashing when an error is detected (Recommended)
    
    ```python
    from kcode import *
    
    text = input("Enter text to encrypt: ")
    
    try:
        encrypted_text = k_code.encode(text)
    except:
        encrypted_text = "ERROR OCCURRED WHEN ENCRYPTING!"
    
    print("Encrypted text: ", encrypted_text)
    ```