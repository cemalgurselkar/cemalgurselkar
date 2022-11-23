toplama = "+"
carpma = "*"
cıkarma = "-"
bölme = "/"

sayı1 = float(input("Birinici sayıyı giriniz: "))
sayı2 = float(input("İkinci sayıyı giriniz: "))
def toplama(sayı1,sayı2):
    return sayı1 + sayı2
def carpma(sayı1,sayı2):
    return sayı1 * sayı2
def cıkarma(sayı1,sayı2):
    return sayı1 - sayı2
def bölme(sayı1,sayı2):
    return sayı1/sayı2
yapılacakislem = input("Yapmak istediğiniz işlemi saçiniz: ")
while True:
    if yapılacakislem == "+":
        print(toplama(sayı1, sayı2))
        break
    elif yapılacakislem == "-":
        print(cıkarma(sayı1, sayı2))
        break
    elif yapılacakislem == "*":
        print(carpma(sayı1, sayı2))
        break
    elif yapılacakislem == "/":
        print(bölme(sayı1, sayı2))
        break
    else:
        print("Hatalı tuşlama yaptınız lütfen tekrar deneyiniz.")
