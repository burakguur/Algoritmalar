sayı = int(input("Bir sayı giriniz: \n"))
bölen = 2
while sayı > 1 :
    if sayı % bölen == 0:
        sayı = sayı / bölen
        print(bölen)
    else:
        bölen += 1
        