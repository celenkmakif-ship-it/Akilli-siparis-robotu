Menu = ["Tavuklu pilav","soslu makarna","köfte","mantı",
        "Kadayıf","baklava","kemalpaşa tatlısı","Künefe",
        "Su","soda","meyve suyu","meyveli soda","Ayran"]

Yemekler = ["Tavuklu pilav","soslu makarna","köfte","mantı"]
Tatlılar = ["Kadayıf","baklava","kemalpaşa tatlısı","Künefe"]
İçecekler = ["Su","soda","meyve suyu","meyveli soda","Ayran"]

print("Restoranımıza Hoşgeldiniz")
print("Buyurun, menümüz")
print(f"Yemeklerimiz: {Yemekler}")
print(f"Tatlılarımız: {Tatlılar}")
print(f"İçeceklerimiz: {İçecekler}")

Toplam_fiyat = 0
Alinanlar = []

Sipariş = input("Ne alırdınız? ")

if Sipariş in Menu:
    Alinanlar.append(Sipariş)
    if Sipariş in Yemekler:
        Toplam_fiyat += 250
    elif Sipariş in Tatlılar:
        Toplam_fiyat += 100
    elif Sipariş in İçecekler:
        Toplam_fiyat += 50
    print(f"{Sipariş} alınmıştır")
else:
    print("Lütfen menüdeki bir şey giriniz")

while True: #Döngü başlatır.
    Fazladan_istek = input("Başka bir şey istiyor musunuz? (İstemiyorsanız 'Tamam' yazın): ")

    if Fazladan_istek == "Tamam":
        break  # Döngü biter, aşağıdaki kodlar (listeye ekleme) çalışmaz.

    if Fazladan_istek in Menu:
        Alinanlar.append(Fazladan_istek)
        if Fazladan_istek in Yemekler:
            Toplam_fiyat += 250
        elif Fazladan_istek in Tatlılar:
            Toplam_fiyat += 100
        elif Fazladan_istek in İçecekler:
            Toplam_fiyat += 50
        print(f"{Fazladan_istek} alınmıştır")
    else:
        print("Lütfen menüdeki bir şey giriniz")

print("\n--- Hesap Özeti ---")
print(f"Toplam Tutar: {Toplam_fiyat} TL")
print(f"Aldığınız Ürünler: {', '.join(Alinanlar)}") # Burada .join() ayırıcı olarak kullanarak bir yinelemeli öğedeki dize öğelerini tek bir dizeye birleştirmeye olanak tanır.
print("İyi günler dileriz!")
