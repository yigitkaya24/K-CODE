class base8:
    def encode(code):

            # girilen kodu binary'e çevir

            binary_form = ''
            for item in code:   binary_form += str(format(ord(item), "08b"))
            
            # base8 alabilmek için 3'ün katı sayıda bit lazım o yüzden sona ekstra bit ekle

            if len(binary_form) % 3 != 0:
                binary_form += (3-(len(binary_form) % 3))*"0"

            # base8 kütüphanesi

            base8_dict = {
                "000": "a",
                "001": "b",
                "010": "c",
                "011": "d",
                "100": "e",
                "101": "f",
                "110": "g",
                "111": "h"
            }

            # elimizdeki binaryi 3bitlik (base8lik) parçalara bölme

            temp_form = binary_form
            binary_form = []

            for i in range(int(len(temp_form)/3)):
                binary_form.insert(len(binary_form), temp_form[0:3])
                temp_form = temp_form[3:]
            
            # 3bitlik kodları base8 diline çevirme

            temp_form = binary_form
            binary_form = ''

            for i in range(len(temp_form)):
                binary_form += base8_dict[temp_form[i]]

            return binary_form

    def decode(code):
        print("future")