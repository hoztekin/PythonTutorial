# Map = bir listedeki her elemana aynı işlemi uygular


sayilar = [1, 2, 3, 4, 5]

# Her sayının karesini al
kareler = list(map(lambda x: x ** 2, sayilar))
print(kareler)  # [1, 4, 9, 16, 25]

# Kelimeleri büyük harfe çevir

kelimeler = ["merhaba", "dünya", "python"]
buyuk = list(map(lambda x: x.upper(), kelimeler))
print(buyuk)  # ['MERHABA', 'DÜNYA', 'PYTHON']

# Her sayıya 10 ekle

sayilar = [1, 2, 3]
sonuc = list(map(lambda x: x + 10, sayilar))
print(sonuc)  # [11, 12, 13]


# Normal fonksiyonla kullanımı
def iki_katini_al(x):
    return x * 2

sayilar = [1, 2, 3, 4]
sonuc = list(map(iki_katini_al, sayilar))
print(sonuc)  # [2, 4, 6, 8]