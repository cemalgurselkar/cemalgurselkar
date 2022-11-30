"""TARİH SINIFI"""

class Tarih:
    aylaragoregunler=[31,29,31,30,31,30,31,31,30,31,30,31]
    aylistesi = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
    def __init__(self,gün,ay,yıl):
        self.ay = int()
        self.gün = int()
        self.yıl = int()
        if ay >=1 and ay<=12:
            self.ay=ay
        else:
            self.ay=1
        if gün>=1 and gün<=self.aylaragoregunler[ay-1]:
            self.gün = gün
        else:
            self.gün=1
        if yıl>=1900 and yıl<=2021:
            self.yıl = yıl
        else:
            self.yıl = 1900
        
    def gunlukArttır(self):
        if self.gun<self.aylaragoregunler[self.ay-1]:
            self.gün += 1
        else:
            self.gün= 1
            if self.ay <12:
                self.ay += 1
            else:
                self.ay = 1
            
    def tarihYazdir(self):
        print("{} {} {}".format(self.gün,self.aylistesi[self.ay-1],self.yıl))

    def tarihKarsılastırma(self,ikinciTarih):
        if self.yıl>ikinciTarih.yıl or self.yıl == ikinciTarih.yıl and self.ay>ikinciTarih.ay or self.yıl == ikinciTarih.yıl and self.ay == ikinciTarih.ay and self.gün > ikinciTarih.gün:
            print("İLk tarih daha büyüktür.")
        elif self.yıl == ikinciTarih.yıl and self.ay == ikinciTarih.ay and self.gün == ikinciTarih.gün:
            print("İki tarih eşittir.")
        else:
            print("İKinci tarih daha büyüktür.")

tarih1 = Tarih(30,8,2002)
tarih2 = Tarih(23, 11, 2013)

tarih1.tarihYazdir()
tarih2.tarihYazdir()
tarih1.tarihKarsılastırma(tarih2)