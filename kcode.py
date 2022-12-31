# encoding:utf-8

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

        base8_dict = {
            "a": "000",
            "b": "001",
            "c": "010",
            "d": "011",
            "e": "100",
            "f": "101",
            "g": "110",
            "h": "111"
        }

        binary_form = ''
        temp_form = code

        for i in range(len(temp_form)):
            binary_form += base8_dict[temp_form[0]]
            temp_form = temp_form[1:]

        if len(binary_form) % 8 != 0:
            binary_form = binary_form[:((len(binary_form) // 8)*8)]

        temp_form = binary_form
        binary_form = []

        for i in range(len(temp_form)//8):
            binary_form.insert(len(binary_form), temp_form[:8])
            temp_form = temp_form[8:]

        temp_form = binary_form
        binary_form = u''

        for i in range(len(temp_form)):
            binary_form += chr(int(temp_form[i], 2))
        return binary_form
        
class matris2D:

    def encode(code):

        # yalnızca yukarıdaki custom base8 kodlarını çevirebilir

        binary_form = []
        temp_form = code

        matris_input = [
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", ""]
        ]

        matris_output = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

        for i in range(len(temp_form)//2):
            binary_form.insert(len(binary_form), [temp_form[0], temp_form[1]])
            temp_form = temp_form[2:]
        
        if temp_form != '':
            binary_form.insert(len(binary_form), [temp_form[0], ''])


        for i in range(len(binary_form)):
            for j in range(len(matris_input)):
                for k in range(len(matris_input[j])):
                    f1 = binary_form[i][0]
                    f2 = binary_form[i][1]
                    if f1 == matris_input[j][k]:
                        binary_form[i][0] = [j, k]
                    if f2 == matris_input[j][k]:
                        binary_form[i][1] = [j, k]


        temp_form = binary_form
        binary_form = []

        for i in range(len(temp_form)):
            binary_form.append(
                [
                    matris_output[temp_form[i][0][0]][temp_form[i][1][1]],
                    matris_output[temp_form[i][1][0]][temp_form[i][0][1]]
                ]
                )

        temp_form = binary_form
        binary_form = ''

        for item in temp_form:
            binary_form += str(item[0]) + str(item[1])

        return binary_form
            
    def decode(code):

        # yalnızca yukarıdaki custom base8 kodlarını çevirebilir

        binary_form = []
        temp_form = code

        matris_input = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

        matris_output = [
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", ""]
        ]


        for i in range(len(temp_form)//2):
            binary_form.insert(len(binary_form), [temp_form[0], temp_form[1]])
            temp_form = temp_form[2:]

        for i in range(len(binary_form)):
            for j in range(len(matris_input)):
                for k in range(len(matris_input[j])):
                    f1 = binary_form[i][0]
                    f2 = binary_form[i][1]
                    if f1 == str(matris_input[j][k]):
                        binary_form[i][0] = [j, k]
                    if f2 == str(matris_input[j][k]):
                        binary_form[i][1] = [j, k]


        temp_form = binary_form
        binary_form = []

        for i in range(len(temp_form)):
            binary_form.append(
                [
                    matris_output[temp_form[i][0][0]][temp_form[i][1][1]],
                    matris_output[temp_form[i][1][0]][temp_form[i][0][1]]
                ]
                )

        temp_form = binary_form
        binary_form = ''

        for item in temp_form:
            binary_form += str(item[0]) + str(item[1])

        return binary_form


class k_code:
    def encode(code):
        temp = base8.encode(code)
        temp = matris2D.encode(temp)
        return temp

    def decode(code):
        temp = matris2D.decode(code)
        temp = base8.decode(temp)
        return temp