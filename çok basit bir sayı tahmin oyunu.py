from random import randint
rand= randint(1,100)
sayac = 0
while True:
    sayac += 1
    sayi = int(input("Düşündüğünüz sayıyı giriniz: "))
    if sayi == 0:
        print("Oyun sonlandırılıyor....")
        break
    elif sayi > rand:
        print("Daha düşük bir sayı giriniz")
        continue
    elif sayi < rand:
        print("Daha büyük bir sayı giriniz")
        continue
    elif sayi == rand:
        print("Tebrikler!!! {} sayısını bildiniz.".format(rand))
        print("{} tane tahmin hakkı kullandınız.".format(sayac))
        break
    
        
