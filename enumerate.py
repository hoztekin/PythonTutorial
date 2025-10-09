
# enumerate() her elemanın hem indeksini hem değerini verir
# İndeks otomatik olarak 0'dan başlar
# for index, meyve in yapısıyla hem indeksi hem değeri alırız

meyveler = ["elma", "armut", "muz", "çilek"]

for index, meyve in enumerate(meyveler):
    print(f"{index}: {meyve}")



# Başlangıç İndeksini Değiştirme

dersler = ["Matematik", "Fizik", "Kimya"]

for sira, ders in enumerate(dersler, start=1):
    print(f"{sira}. ders: {ders}")


# Enumerate Olmadan
isimler = ["Ali", "Ayşe", "Mehmet"]

for i in range(len(isimler)):
    print(f"{i}: {isimler[i]}")

# Enumerate İle
isimler = ["Ali", "Ayşe", "Mehmet"]

for i, isim in enumerate(isimler):
    print(f"{i}: {isim}")


# Belirli Elemanları Bulmak
notlar = [45, 78, 92, 55, 88]

for index, not_degeri in enumerate(notlar):
    if not_degeri >= 90:
        print(f"İndeks {index}'deki not takdir aldı: {not_degeri}")


# Dictionary Oluşturmak
isimler = ["Ahmet", "Zeynep", "Can"]

isim_dict = {index: isim for index, isim in enumerate(isimler)}
print(isim_dict)


# Enumerate'i Liste Olarak Almak
renkler = ["kırmızı", "mavi", "yeşil"]

enumerate_list = list(enumerate(renkler))
print(enumerate_list)

# Nested (İç İçe) Listelerle Enumerate
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for satir_index, satir in enumerate(matris):
    for sutun_index, deger in enumerate(satir):
        print(f"[{satir_index}][{sutun_index}] = {deger}")