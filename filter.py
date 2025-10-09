# Filter = koşulu sağlayan elemanları seçer

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sadece çift sayıları al
cift = list(filter(lambda x: x % 2 == 0, sayilar))
print(cift)  # [2, 4, 6, 8, 10]


# 50'den büyük sayılar
sayilar = [23, 65, 19, 90, 105, 44]
buyukler = list(filter(lambda x: x > 50, sayilar))
print(buyukler)  # [65, 90, 105]


# Uzun kelimeleri seç (5+ harf)
kelimeler = ["ev", "araba", "at", "bilgisayar"]
uzun = list(filter(lambda x: len(x) >= 5, kelimeler))
print(uzun)  # ['araba', 'bilgisayar']

