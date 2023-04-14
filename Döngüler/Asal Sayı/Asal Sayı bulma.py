sayı = int(input("Bir sayı giriniz: \n"))

bölen = 2

asalKontrol = 0

for sayac in range(2, sayı//2+1):
    if sayı % sayac == 0:
        asalKontrol = 1

if asalKontrol == 0:
    print(("Sayınız Asal Sayıdır."))

else:
    print("Sayınız Asal Sayı değildir.")
