sayi = int(input("Sayı giriniz: "))
faktoriyel = 1

for sayac in range(1, sayi+1):
    faktoriyel *= sayac
print(f"Sonucunuz: {faktoriyel}")