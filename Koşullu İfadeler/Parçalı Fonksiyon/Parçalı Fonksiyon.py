print("X değerini giriniz")
x = float(input())
if x < 1:
    y = 3 * x - 4
else:
    if x >= 1 and x <= 10:
        y = x + 2
    else:
        if x > 10:
            y = 2 * x + 4
print("Fonksiyon Sonucu: " + str(y))
