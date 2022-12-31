from kcode import *

while True:
    a = input("Enter a number: ")
    a = k_code.encode(a)
    print(a)
    a = k_code.decode(a)
    print(a)