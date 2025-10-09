# Reduce = listeyi tek değere indirger

# Önce import et
from functools import reduce

sayilar = [1, 2, 3, 4, 5]

# Tüm sayıları topla
toplam = reduce(lambda x, y: x + y, sayilar)
print(toplam)  # 15

# Tüm sayıları çarp
sayilar = [1, 2, 3, 4]
carpim = reduce(lambda x, y: x * y, sayilar)
print(carpim)  # 24 (1*2*3*4)

# En büyük sayıyı bul
sayilar = [5, 2, 8, 1, 9, 3]
maks = reduce(lambda x, y: x if x > y else y, sayilar)
print(maks)  # 9

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Filter: Çift sayıları seç
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print("Çift sayılar:", ciftler)  # [2, 4, 6, 8, 10]

# 2. Map: Her birinin karesini al
kareler = list(map(lambda x: x ** 2, ciftler))
print("Kareleri:", kareler)  # [4, 16, 36, 64, 100]

# 3. Reduce: Hepsini topla
toplam = reduce(lambda x, y: x + y, kareler)
print("Toplam:", toplam)  # 220


