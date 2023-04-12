pozitif = 0
negatif = 0
adet = int(input("Adet giriniz: "))


for i in range(1, adet+1):
    sayı = int(input("Sayı giriniz: "))

    if sayı > 0 :
        pozitif +=1
    elif sayı <0:
        negatif +=1

print(f"Pozitif sayı adedi: {pozitif}\n Negatif sayı adedi: {negatif}")