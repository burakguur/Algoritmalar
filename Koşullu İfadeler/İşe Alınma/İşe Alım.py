print("Yaşınızı Giriniz")
yas = int(input())
if yas < 35:
    print("Sürücü Belgeniz Var Mı E/H")
    surucuBelgesi = input()
    print("Üniversite Mezunu musunuz? E/H")
    ogrenimDurumu = input()
    if surucuBelgesi == "E" and ogrenimDurumu == "E":
        print("İşe Alındınız")
    else:
        print("Üzgünüz İşe Alınmadınız")
else:
    print("Üzgünüz İşe Alınmadınız")
