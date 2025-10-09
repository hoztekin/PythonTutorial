# NumPy Hakkında Özet
# NumPy (Numerical Python), Python'da bilimsel hesaplama için kullanılan temel kütüphanedir. Çok boyutlu diziler (arrays) ve matrisler üzerinde hızlı işlemler yapmayı sağlar.
# Temel Özellikler:
#
# Sabit tip veri tutar ✓ (Evet, homogeneous - tüm elemanlar aynı veri tipinde olmalı)
# C dilinde yazılmış çekirdeği sayesinde çok hızlı
# Bellekte verimli depolama
# Vektörize işlemler (döngü yazmadan toplu işlem)
#
# Sık Kullanılan Metotlar ve Örnekler:


import numpy as np

# 1. DİZİ OLUŞTURMA
arr1 = np.array([1, 2, 3, 4, 5])  # Liste'den array
arr2 = np.zeros((3, 4))            # Sıfırlarla dolu 3x4 array
arr3 = np.ones((2, 3))             # Birlerle dolu 2x3 array
arr4 = np.arange(0, 10, 2)         # 0'dan 10'a 2'şer artarak [0,2,4,6,8]
arr5 = np.linspace(0, 1, 5)        # 0-1 arası 5 eşit parça
arr6 = np.random.rand(3, 3)        # 3x3 rastgele sayılar (0-1 arası)

# 2. ARRAY ÖZELLİKLERİ
print(arr1.shape)      # Boyut: (5,)
print(arr1.dtype)      # Veri tipi: int64
print(arr1.ndim)       # Boyut sayısı: 1
print(arr1.size)       # Toplam eleman sayısı: 5

# 3. RESHAPE (Yeniden Şekillendirme)
arr = np.arange(12)
reshaped = arr.reshape(3, 4)  # 12 elemanlı diziyi 3x4 matrise çevir

# 4. MATEMATİKSEL İŞLEMLER
arr = np.array([1, 2, 3, 4, 5])
print(arr.sum())       # Toplam: 15
print(arr.mean())      # Ortalama: 3.0
print(arr.std())       # Standart sapma
print(arr.min())       # Minimum: 1
print(arr.max())       # Maksimum: 5
print(arr.argmax())    # Maksimum değerin indeksi: 4

# 5. DİZİ İŞLEMLERİ (Vektörize)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)     # [5, 7, 9] - Eleman eleman toplama
print(arr1 * arr2)     # [4, 10, 18] - Eleman eleman çarpma
print(arr1 ** 2)       # [1, 4, 9] - Karesini alma

# 6. İNDEXLEME ve SLICING
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0, 1])       # 2 - Satır 0, Sütun 1
print(arr[1:, :2])     # İlk 2 sütun, 1. satırdan sonrası
print(arr[arr > 5])    # [6, 7, 8, 9] - Koşullu indexleme

# 7. MATRIS İŞLEMLERİ
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
print(mat1.T)          # Transpose (devrik)
print(np.dot(mat1, mat2))  # Matris çarpımı
print(mat1.flatten())  # 1D diziye çevir: [1, 2, 3, 4]

# 8. İSTATİSTİKSEL İŞLEMLER
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.sum(axis=0))     # Sütunlara göre toplam: [5, 7, 9]
print(arr.sum(axis=1))     # Satırlara göre toplam: [6, 15]
print(np.median(arr))      # Medyan
print(np.percentile(arr, 75))  # 75. yüzdelik dilim

# 9. DİĞER KULLANIŞLI METOTLAR
arr = np.array([3, 1, 2, 5, 4])
print(np.sort(arr))        # Sıralama: [1, 2, 3, 4, 5]
print(np.unique([1, 1, 2, 3, 2]))  # Benzersiz değerler: [1, 2, 3]
print(np.concatenate([arr1, arr2]))  # Dizileri birleştir
print(np.where(arr > 3))   # 3'ten büyük elemanların indeksleri



# Sabit Tip Veri Yapısı
# Tüm elemanlar aynı tipte olmalı

arr_int = np.array([1, 2, 3])        # dtype: int64
arr_float = np.array([1.0, 2.0, 3.0])  # dtype: float64

# Karışık tip verirseniz, NumPy otomatik dönüştürür
arr_mixed = np.array([1, 2.5, 3])    # Hepsi float'a dönüşür: dtype: float64

# Tip belirtebilirsiniz
arr = np.array([1, 2, 3], dtype=np.float32)


# NumPy Array'leri Tuple ve Dictionary'den Oluşturma

import numpy as np

# 1D tuple'dan array
my_tuple = (1, 2, 3, 4, 5)
arr = np.array(my_tuple)
print(arr)  # [1 2 3 4 5]
print(type(arr))  # <class 'numpy.ndarray'>

# İç içe tuple'dan 2D array
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
arr_2d = np.array(nested_tuple)
print(arr_2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Tuple listesinden
tuple_list = [(1, 2), (3, 4), (5, 6)]
arr = np.array(tuple_list)
print(arr)
# [[1 2]
#  [3 4]
#  [5 6]]

# Dictionary'nin kendisini direkt array'e çeviremezsiniz çünkü key-value yapısı array formatına uygun değil. Ama dictionary'nin değerlerini veya anahtarlarını kullanarak array oluşturabilirsiniz:

import numpy as np

# Dictionary örneği
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 1. SADECE DEĞERLERİ AL
arr_values = np.array(list(my_dict.values()))
print(arr_values)  # [1 2 3 4]

# 2. SADECE ANAHTARLARI AL
arr_keys = np.array(list(my_dict.keys()))
print(arr_keys)  # ['a' 'b' 'c' 'd']

# 3. STRUCTURED ARRAY (Key-Value çiftlerini saklama)
# Bu daha gelişmiş bir yöntem
data = list(my_dict.items())
arr_structured = np.array(data, dtype=[('key', 'U10'), ('value', 'i4')])
print(arr_structured)
# [('a', 1) ('b', 2) ('c', 3) ('d', 4)]

# 4. İÇİÇE DİCTIONARY (Tablo benzeri)
data_dict = {
    'isim': ['Ali', 'Ayşe', 'Mehmet'],
    'yaş': [25, 30, 35],
    'maaş': [5000, 6000, 7000]
}

# Her bir değeri ayrı array olarak
for key, value in data_dict.items():
    arr = np.array(value)
    print(f"{key}: {arr}")

# isim: ['Ali' 'Ayşe' 'Mehmet']
# yaş: [25 30 35]
# maaş: [5000 6000 7000]

# 5. RECORD ARRAY (Pandas benzeri)
arr_record = np.array(
    [('Ali', 25, 5000), ('Ayşe', 30, 6000), ('Mehmet', 35, 7000)],
    dtype=[('isim', 'U10'), ('yaş', 'i4'), ('maaş', 'i4')]
)
print(arr_record['isim'])  # ['Ali' 'Ayşe' 'Mehmet']
print(arr_record['yaş'])   # [25 30 35]


# Not: Dictionary ile çalışacaksanız genelde Pandas kütüphanesi daha uygun olur, çünkü DataFrame yapısı dictionary benzeri veri için optimize edilmiştir!


# NumPy'da Negatif (Eksi) Index KullanımıNegatif indexler sondan başa doğru saymaya yarar. -1 son eleman, -2 sondan ikinci eleman demektir.


import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# POZİTİF INDEX (baştan)
print(arr[0])    # 10 (ilk eleman)
print(arr[1])    # 20
print(arr[6])    # 70 (son eleman)

# NEGATİF INDEX (sondan)
print(arr[-1])   # 70 (son eleman)
print(arr[-2])   # 60 (sondan 2.)
print(arr[-3])   # 50 (sondan 3.)
print(arr[-7])   # 10 (sondan 7. = ilk eleman)


# Görsel Açıklama:
# Array:     [10,  20,  30,  40,  50,  60,  70]
# Pozitif:     0    1    2    3    4    5    6
# Negatif:    -7   -6   -5   -4   -3   -2   -1


# 2D Array'de Negatif Index
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Son satır, son sütun
print(arr2d[-1, -1])   # 9

# Son satır, ilk sütun
print(arr2d[-1, 0])    # 7

# İlk satır, son sütun
print(arr2d[0, -1])    # 3

# Sondan 2. satır, sondan 2. sütun
print(arr2d[-2, -2])   # 5