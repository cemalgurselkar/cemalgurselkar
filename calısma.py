"""
urun1 = input("1.ürün= ")
urun2 = input("2.ürün= ")
urun3 = input("3.ürün= ")
urun4 = input("4.ürün= ")
urun5 = input("5.ürün= ")
urun6 = input("6.ürün= ")
urun7 = input("7.ürün= ")
urun8 = input("8.ürün= ")
urun9 = input("9.ürün= ")
urun10 = input("10.ürün= ") 
toplamfiyat = float(urun1) + float(urun2) + float(urun3) + float(urun4) + float(urun5) + float(urun6) + float(urun7) + float(urun8) + float(urun9) + float(urun10)
ödenenpara = input("ödenenpara= ")
paraustu = float(ödenenpara) - float(toplamfiyat)
print(paraustu)
"""
#name = "cemal"
#surname = "kar"
#print("My name is {} {}".format(name,surname))

#name = input("isim= ")

#print("My name is {}".format(name))
"""
result = 200 / 650
print("the result {}".format(result))
"""
message = "My name is Cemal Gursel"
#message = message.upper()
#message = message.lower()
#message = message.capitalize()
#message = message.strip()
#message = message.split()
#isFound = message.startswith("c")
#isFound = message.endswith("l")
#print(isFound)
"""
list1 = [1,2,3,4]
list2 = [5,6,7,8]
numbers = list1 + list2
print(len(numbers))
print(numbers[2])
"""

#numbers = [1,2,3,4,5,6,7,8]

#numbers.append(10)----- sayı ekleme 
#numbers.insert(4,42)------- belli bölgeye sayı ekleme
#numbers.pop(2)------ silme işlemi
#numbers.remove(6)------kaldırma işlemi
#numbers.sort()------küçükten büyüge sıralanır
#numbers.reverse()
#numbers.extend()------- başka bir küme ekleme
#print(numbers)
#demetlere ekleme yapılamaz aynı kalmak zorunda





"""
sehirler = ["Mersin", "Adana"]
plakalar = [33, 1]
print(plakalar[sehirler.index("Mersin")])
print(sehirler[plakalar.index(33)])
"""

"""
plakalar = {'Mersin' : 33, 'Adana' : 1}
print(plakalar["Mersin"])
print(plakalar["Adana"])
"""
"""
#notunu giriniz
x = input("Notunuzu giriniz=  ")
if float(x)>= 80:
    print("Notunuz: A")
elif float(x)<80 and float(x)>=60:
    print("Notunuz: B")
elif float(x)<60 and float(x)>=40:
    print("Notunuz: C")
else:
    print("Notunuz: F")
"""
"""
liste = [1,2,3,4,5,6,7]

a = 5
if a in liste:
    print("listede var")
else:
    print("listede yok")
"""
#demet = ("sarı", "kırmızı", "yesil", "mor","siyah","pembe","turuncu","mavi" )
#küme1 = {"sarı", "kırmızı", "yesil", "mor","siyah","pembe","turuncu","mavi"}
#küme.add("beyaz")
#küme.remove("sarı")
#küme.discard("gri")-------farkı remove hata veriyor kümede yoksa
#küme1.intersection(küme2)------------- ortak elemanları sıralama
#küme1.union(küme2)-------- birleştirme
#küme1.difference(küme2)---------farkını göster
#set()--------- kümeye çevirir
"""
x = input("Notunuzu giriniz:  ")
if float(x)>=80:
    print("Notunuz: A")
elif float(x)<80 and float(x)>=60:
    print("Notunuz: B")
elif float(x)<60 and float(x)>=40:
    print("Notunuz: C")
else:
    print("Notunuz: F")
"""
"""
liste = ["a","b","c"]
liste2 = [1,2,3]
for harf in liste:
    for rakam in liste2:
        print(harf,rakam)
"""        
"""
x = 1
while True:
    print(x)
    x += 1
    if x == 1000:
        break
    print("x= ",x)
"""
"""
i = 1
while True:
    if i % 2 ==0:
        i += 1
        continue
    print(i)
    i += 1
    if i == 1000:
        break
"""
"""
sayı = int(input("Sayı giriniz: "))
faktoriyel = 1
for i in range(1, sayı +1):
    faktoriyel *= i
print(f"{sayı}! = {faktoriyel}")
"""
"""
sayı = int(input("Bir sayı giriniz: "))

faktoriyel = 1
i = 2
while i <= sayı:
    faktoriyel *= i
    i += 1
print(f"{sayı}! = {faktoriyel}")
"""
"""
sayı  = int(input("Bir sayı giriniz: "))

prime = True

for i in range(2,sayı):
   if sayı %i == 0:
    prime = False
    break
if prime == True:
    print(f"{sayı} sayısı asaldır")
else:
    print(f"{sayı} sayısı asal değildir")
"""    
"""
sayı = int(input("Bir sayı giriniz: "))

bolen_sayısı = 0

for i in range(1, sayı + 1):
    if sayı %i == 0:
        bolen_sayısı += 1
print(f"{sayı} sayısının {bolen_sayısı} tane sayısı vardır.")
"""
"""
sayı = int(input("Bir sayı giriniz: "))

bolen_sayısı = 0

for i in range(1,sayı + 1):
    if sayı % i == 0:
        bolen_sayısı += 1
print(f"{sayı} sayısının {bolen_sayısı} tane böleni vardır.")
"""
"""
sayı = int(input("Bir sayı giriniz: "))

str_sayı = str(sayı)
toplam = 0

for rakam in str_sayı:
    toplam += int(rakam)
print(toplam)
"""
"""
liste = []

for i in range(5):
    sayı = int(input("Bir sayı giriniz: "))
    liste.append(sayı)

print(f"En büyük sayı: {max(liste)}")
print(f"En kücük sayı : {min(liste)}")
"""
"""
sayı = int(input("Bir sayı giriniz: "))

karekok = sayı ** 0.5

if karekok == int(karekok):
    print("Tamkare")
else:
    print("Tamkare değil")
"""
"""
metin = str(input("Bir metin yazınız:   "))
sozluk = dict()

for harf in metin:
    if harf in sozluk :
        sozluk[harf] += 1
    else:
        sozluk[harf] = 1
for harf,adet in sozluk.items():
    print(harf,adet)
"""
"""
prime_liste = list()

prime_liste.append(2)

sayi = 3 
while True:
    prime = True
    for i  in range(2,sayi):
        if sayi %i ==0:
            prime = False
            break
    if prime:
        prime_liste.append(sayi)
        if len(prime_liste) == 100:
            break
    sayi += 1
list2 = []
for prime in prime_liste:
    strprime = str(prime)
    if strprime.startswith("3") and strprime.endswith("7"):
        list2.append(prime)
print(list2)
print(len(list2))
"""

"""
liste = []
for sayi in range(100,1000):
    toplam = 0
    gecici_sayi = sayi
    while gecici_sayi != 0:
        basamak  = gecici_sayi % 10
        toplam += basamak ** 3
        gecici_sayi //= 10
    if toplam == sayi:
        liste.append(sayi)
print(liste)
"""
"""
para = int(input("Lütfen bir para miktarı giriniz: "))
print("{} adet 200 tl var.".format(para//200))
para%=200
print("{} adet 100 tl var.".format(para//100))
para%=100
print("{} adet 50 tl var.".format(para//50))
para%=50
print("{} adet 20 tl var.".format(para//20))
para%=20
print("{} adet 10 tl var.".format(para//10))
para%=10
"""
"""
sayı = int(input("Bir sayı giriniz: "))
print(sayı%10,end="")
sayı = sayı//10
print(sayı%10,end="")
sayı = sayı//10
print(sayı%10,end="")
sayı = sayı//10
"""
"""
yapılacakişlem = input("LÜtfen yapılacak işlem öperatörünü seçiniz: ")
if yapılacakişlem== '+' or yapılacakişlem== '-' or yapılacakişlem== '*' or yapılacakişlem== '/':
    sayı1,sayı2= map(float,input("LÜtfen 2 adet sayı giriniz: ").split(","))
    if yapılacakişlem== '+':
        sonuc= sayı1 + sayı2
        print(sonuc)
    elif yapılacakişlem== '-':
        sonuc= sayı1 - sayı2
        print(sonuc)
    elif yapılacakişlem== '*':
       sonuc= sayı1 * sayı2
       print(sonuc)
    elif yapılacakişlem== '/':
        sonuc= sayı1/sayı2
        print(sonuc)
else:
    print("Hatalı işlem girdiniz. Lütfen tekrar deneyiniz.")
"""
"""
bakiye = 10000
paracekme: 1
parayatırma: 2
yapılacakişlem = int(input("Yapılacak işlemi seçiniz: "))
if yapılacakişlem == 1 :
    çekilecekpara= int(input("Çekilecek para miktarını giriniz: "))
    if int(bakiye) < int(çekilecekpara):
        print("Yetersiz para")
    else:
        kalanbakiye = bakiye - çekilecekpara
        print("İşlem başarılı.\nKalan tutarınız {}'dir.".format(kalanbakiye))
if yapılacakişlem == 2:
    yatırılacakpara = int(input("Lütfen yatıracağınız tutarı giriniz: "))
    yenibakiye = bakiye + yatırılacakpara
    print("İşlem başarılıdır.\nYeni bakiyeniz {}'dir".format(yenibakiye))
else:
    print("Hatalı islem seçtiniz. Lütfen yeniden deneyiniz.") 
"""
"""
sayı = int(input("Bir sayı giriniz: "))
faktoriyel = 1
i = 2
while i<= sayı:
    faktoriyel *=i
    i +=1 
print("{}!={} ".format(sayı,faktoriyel))
"""
"""
sayı= int(input("Bir sayı giriniz: "))
bolundumu = False
for i in range(2,sayı):
    if sayı%i ==0:
        bolundumu = True
        break
if bolundumu == False:
    print("{} sayısı asaldır.".format(sayı))
else:
    print("{} sayısı asal değildir.".format(sayı))
"""
"""
sayı = int(input("Bir sayı giriniz: "))
gecicisayı = sayı
sayınıntersi = 0

while gecicisayı != 0:
    kalan = gecicisayı%10
    sayınıntersi = sayınıntersi*10 + kalan
    gecicisayı//=10
print("{} sayısının tersi {}'dir.".format(sayı,sayınıntersi))
"""
"""
sayı = int(input("Bir limit belirleyiniz: "))
i = 1
x = str()
while True:
    print("x"*i)
    i+= 1
    if len(("x")*i) == sayı:
        break
"""
"""
kucukharf = False
buyukharf = False
sayısorgula = False
karaktersayısı = 0
sifre = input("Bir şifre giriniz: ")
for ch in sifre:
    if kucukharf==False and ch >="a" and ch <="z":
        kucukharf = True
    elif buyukharf==False and ch >="A" and ch<= "Z":
        buyukharf = True
    elif sayısorgula== False and ch>= "0" and ch <= "9":
        sayısorgula= True
    karaktersayısı += 1
if buyukharf==False:
    print("Büyük harf eksik")
elif kucukharf==False:
    print("Kücük harf eksik")
elif sayısorgula==False:
    print("Sayı kullanımı gereklidir.")
elif len(sifre)<=8:
    print("Yetersiz karakter")
elif len(sifre)>=16:
    print("Fazla karakter kullanımı")
else:
    print("Şifre kabul edildi.")
"""
# FUCNTİNOS
"""def selamla(isim,soyisim):
    print("Merhaba",isim,soyisim)
selamla("cemal", "gursel")"""
"""def sayılar(*sayılar):
    for sayı in sayılar:
        print(sayı,end=" ")
    print(end="\n")
sayılar(1,2,5,2,643,3,633,6,72,886)"""
"""def listeler(liste):
    liste.sort()
    enkucuk = liste[-1]
    enbuyuk = liste[0]
    return enkucuk,enbuyuk
sonuc = listeler([1,2,5,7,8,3,7,24,75,4,3452,5])
print(sonuc)"""
"""
def harfdegiştir(cümle,eskiharf,yeniharf):
    cümle=list(girilencümle)
    for indis in range(len(cümle)):
        if cümle[indis] == eskiharf:
            cümle[indis] = yeniharf
    return cümle

girilencümle = input("Bir cümle giriniz: ")
eskiharf,yeniharf = input("Değiştirelecek harfleri sırasıyla giriniz: ").split(",")
girilencümle= str(harfdegiştir(girilencümle,eskiharf,yeniharf))
print(girilencümle)"""

"""def harfdeğiştir(cümle):
    cümle = list(cümle)
    cümle[0]= cümle[0].upper
    for indis in range(len(cümle)):
        if cümle[indis] == '.':
            indis +=1
            cümle[indis] = cümle[indis].upper()
    return cümle

girilencümle = input("Bir cümle giriniz: ")
girilencümle = str(harfdeğiştir(girilencümle))
print(girilencümle)
"""

"""def anagramKontrol(kelime1,kelime2):
    if len(kelime1) != len(kelime2):
        return False
    kelime1list,kelime2list = list(kelime1), list(kelime2)
    kelime1list.sort()
    kelime2list.sort()
    for indis in range(len(kelime1list)):
        if kelime1list[indis] != kelime2list[indis]:
            return False
    return True

print(anagramKontrol("sfgkmsflkdg", "asgslg"))"""

"""def pelidrom(string):
    stringters = string[::-1]
    if stringters == string:
        return True
    else:
        return False
print(pelidrom("cekel"))"""

"""def fibonacciyazdırma(sayı):
    if sayı == 0 or sayı == 1:
        return sayı
    else:
        return fibonacciyazdırma(sayı-1)+fibonacciyazdırma(sayı-2)
print(fibonacciyazdırma(19))"""

"""def ortalamakelimehesapla(string):
    toplamkelime = 0
    toplamkarakter = 0
    for ch in string:
        if ch==" ":
            toplamkelime +=1
        toplamkarakter +=1
    toplamkelime +=1
    print("Toplam karakter sayısı {} ve toplam kelime sayısı {}".format(toplamkarakter,toplamkelime))
    return toplamkarakter/toplamkelime
print(ortalamakelimehesapla("cemal gursel kar"))"""

#zip fonksiyonu
#birbirinden farklı listeleri birleştirme 
"""liste1 = [i for i in range(10)]
liste2 = [j for j in range(10,20)]
liste3 = ["a","b","c","d","e","r","g"]
x = list(zip(liste1,liste2,liste3))
print(x)"""
#map fonksiyonu
# bir iterasyon yapsıındaki elemanların hepsine aynı değişikliği uygulamak
"""liste1 = [i for i in range(10)]
liste2 = [j for j in range(10,20)]
def kupal(x,y):
    return x**3,y**3
for i,j in map(kupal,[i for i in range(10)],[j for j in range(10,20)]):
    print(i,j)
"""
"""from turtle import Turtle, Screen
wn = Screen()
def tree(length,t):
    if length > 5:
        t.forward(length) # ileri git
        t.right(40)       # sağa dön
        tree(length-15,t) # daha küçük bir ağaç çiz
        t.left(80)        # sola dön
        tree(length-15,t) # daha küçük bir ağaç çiz
        t.right(40)       # Başladığın açıya geri dön
        t.backward(length)# Başladığın noktaya geri dön
t = Turtle()
t.left(90) # Yukarıya doğru çizmek için
t.speed(0) # en hızlı animasyon
tree(100,t)
wn.exitonclick()"""

"""kelimesayısıdosyası = open("örnek2.txt", "r")
dosyaicerigi = kelimesayısıdosyası.read()
kelimesayısı = dosyaicerigi.split(" ")
print(len(kelimesayısı)"""

"""dosya = open("örnek.txt", mode="r")
dosya2 = open("örnek2.txt","w")

dosyaicerigi = dosya.read()
dosyaicerigi = dosyaicerigi.upper()
dosya2.write(dosyaicerigi)
dosya.close()
dosya2.close()"""

"""dosya3 = open("öğrencinötları.txt","w")
dosya3.write("Cemal gürsel,kar,75,95\nFatma ceren,kar,90,95\nSaliha,keller,65,75\nfatma,keller,50,45")
dosya3.close()
dosya = open("öğrencinotları.txt","r")
dosya2 = open("öğrencinotları2.txt","w")
öğrencibilgileri = dosya.readlines()
for öğrencibilgi in öğrencibilgileri:
    ad,soyad,vize,final=öğrencibilgi.split(",")
    vize,final = int(vize), int(final)
    ortalama  = vize*0.4 + final*0.6
    harfnotu = str()
    basarıdurumu = str()
    if ortalama >=90:
        harfnotu += "A"
    elif ortalama >=80:
        harfnotu += "B"
    elif ortalama >=70:
        harfnotu += "C"
    elif ortalama >= 60:
        harfnotu +="D"
    else:
        harfnotu += "F"
yazılacakbilgi ="ad,soyad: {} {}. vizesi: {} , finali: {}. Ortalaması: {}. Harf notu: {}.\n".format(ad,soyad,vize,final,ortalama,harfnotu)
dosya2.write(yazılacakbilgi)
dosya.close()
dosya2.close()"""

"""from turtle import *
speed(200)
color("cyan")
bgcolor("black")
b = 200
while b > 0:
    left(b)
    forward(b*2)
    b = b - 1
    
print(b)"""
