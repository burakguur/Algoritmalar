sayi = int(input("Bir sayı giriniz."))
carpan_toplamı = 0

for sayac in range(1, sayi // 2 + 1):
    if sayi % sayac == 0:
        carpan_toplamı += sayac
if sayi == carpan_toplamı:
    print("Sayınız mükemmel sayıdır.")
else:
    print("Sayınız mükemmel sayı değildir.")
