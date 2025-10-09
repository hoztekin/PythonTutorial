# Pandas Nedir?
# Pandas, Python'da veri analizi ve manipülasyonu için en çok kullanılan kütüphanedir. Excel tablolarına benzer şekilde verilerle çalışmanızı sağlar.

# Kurulum
# pip install pandas

# İçe aktarma
import pandas as pd

# Series (Tek boyutlu)
# Series oluşturma

s = pd.Series([10, 20, 30, 40, 50])
print(s)

# İsimlendirilmiş index ile
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s['a'])  # 10

# DataFrame (İki boyutlu - Tablo)
# Dictionary'den DataFrame
data = {
    'İsim': ['Ahmet', 'Ayşe', 'Mehmet', 'Fatma'],
    'Yaş': [25, 30, 35, 28],
    'Şehir': ['İstanbul', 'Ankara', 'İzmir', 'Bursa'],
    'Maaş': [5000, 6000, 5500, 4800]
}
df = pd.DataFrame(data)
print(df)

# Veri Okuma ve Yazma

# CSV okuma
df = pd.read_csv('veriler.csv')
df = pd.read_csv('veriler.csv', encoding='utf-8')
df = pd.read_csv('veriler.csv', sep=';')  # Farklı ayırıcı

# Excel okuma
df = pd.read_excel('veriler.xlsx', sheet_name='Sayfa1')

# JSON okuma
df = pd.read_json('veriler.json')

# SQL okuma
import sqlite3
conn = sqlite3.connect('veritabani.db')
df = pd.read_sql('SELECT * FROM tablo', conn)

# Veri yazma
df.to_csv('yeni_veri.csv', index=False)
df.to_excel('yeni_veri.xlsx', index=False)
df.to_json('yeni_veri.json')


# Veri İnceleme (En Çok Kullanılanlar!)

# İlk/son satırları görme
df.head()      # İlk 5 satır
df.head(10)    # İlk 10 satır
df.tail()      # Son 5 satır

# Boyut bilgisi
df.shape       # (satır, sütun)
df.info()      # Veri tipleri ve null değerler
df.describe()  # İstatistiksel özet

# Sütun isimleri
df.columns

# Veri tipleri
df.dtypes

# Null değer kontrolü
df.isnull().sum()
df.isna().sum()

# Benzersiz değerler
df['Şehir'].unique()
df['Şehir'].nunique()  # Benzersiz değer sayısı
df['Şehir'].value_counts()  # Frekans tablosu


# Veri Seçme ve Filtreleme

# Sütun seçme
df['İsim']              # Tek sütun (Series)
df[['İsim', 'Yaş']]     # Çoklu sütun (DataFrame)

# Satır seçme (iloc - index numarası ile)
df.iloc[0]              # İlk satır
df.iloc[0:3]            # İlk 3 satır
df.iloc[:, 0:2]         # Tüm satırlar, ilk 2 sütun

# Satır seçme (loc - index etiketi ile)
df.loc[0:2]             # 0,1,2 indeksli satırlar
df.loc[0:2, 'İsim':'Yaş']  # Belirli satır ve sütunlar

# Koşullu filtreleme (ÇOK ÖNEMLİ!)
df[df['Yaş'] > 28]                        # Yaşı 28'den büyük
df[df['Şehir'] == 'İstanbul']             # İstanbul'da olanlar
df[(df['Yaş'] > 25) & (df['Maaş'] > 5000)]  # VE koşulu (&)
df[(df['Şehir'] == 'İstanbul') | (df['Şehir'] == 'Ankara')]  # VEYA (|)

# isin() ile filtreleme
df[df['Şehir'].isin(['İstanbul', 'Ankara'])]

# String içerenleri bulma
df[df['İsim'].str.contains('Ah')]
df[df['İsim'].str.startswith('A')]

# Veri Manipülasyonu

# Yeni sütun ekleme
df['Yıllık_Maaş'] = df['Maaş'] * 12
df['Yaş_Grubu'] = df['Yaş'].apply(lambda x: 'Genç' if x < 30 else 'Orta Yaş')

# Sütun silme
df.drop('Yıllık_Maaş', axis=1, inplace=True)
df.drop(['Sütun1', 'Sütun2'], axis=1, inplace=True)

# Satır silme
df.drop(0, axis=0, inplace=True)  # 0. indexli satırı sil

# Sütun adı değiştirme
df.rename(columns={'İsim': 'Ad', 'Yaş': 'Yas'}, inplace=True)

# Veri tipi değiştirme
df['Yaş'] = df['Yaş'].astype(int)
df['Maaş'] = df['Maaş'].astype(float)

# Sıralama
df.sort_values('Yaş')                          # Artan
df.sort_values('Yaş', ascending=False)         # Azalan
df.sort_values(['Şehir', 'Yaş'])              # Çoklu sıralama

# Index sıfırlama
df.reset_index(drop=True, inplace=True)


# Veri Temizleme

# Null değerleri silme
df.dropna()              # Tüm null'ları sil
df.dropna(subset=['Yaş'])  # Belirli sütundaki null'ları sil

# Null değerleri doldurma
df.fillna(0)                     # 0 ile doldur
df.fillna(df.mean())             # Ortalama ile doldur
df['Yaş'].fillna(df['Yaş'].mean())  # Belirli sütunu doldur
df.fillna(method='ffill')        # Önceki değerle doldur
df.fillna(method='bfill')        # Sonraki değerle doldur

# Tekrar eden satırları silme
df.drop_duplicates()
df.drop_duplicates(subset=['İsim'])  # Belirli sütuna göre

# String temizleme
df['İsim'] = df['İsim'].str.strip()      # Boşlukları temizle
df['İsim'] = df['İsim'].str.lower()      # Küçük harf
df['İsim'] = df['İsim'].str.upper()      # Büyük harf
df['İsim'] = df['İsim'].str.replace('Ah', 'A')  # Değiştir


# Gruplama ve Aggregation

# Gruplama
df.groupby('Şehir')['Maaş'].mean()           # Şehre göre ortalama maaş
df.groupby('Şehir')['Maaş'].sum()            # Toplam
df.groupby('Şehir')['Maaş'].count()          # Sayım
df.groupby('Şehir')['Maaş'].max()            # Maximum

# Çoklu aggregation
df.groupby('Şehir').agg({
    'Maaş': ['mean', 'sum', 'count'],
    'Yaş': ['min', 'max']
})

# Pivot tablo
df.pivot_table(
    values='Maaş',
    index='Şehir',
    columns='Yaş_Grubu',
    aggfunc='mean'
)

# Birleştirme İşlemleri

# İki DataFrame'i birleştirme
df1 = pd.DataFrame({'ID': [1, 2, 3], 'İsim': ['Ahmet', 'Ayşe', 'Mehmet']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Maaş': [5000, 6000, 5500]})

# Merge (SQL JOIN gibi)
pd.merge(df1, df2, on='ID', how='inner')   # Inner join
pd.merge(df1, df2, on='ID', how='left')    # Left join
pd.merge(df1, df2, on='ID', how='right')   # Right join
pd.merge(df1, df2, on='ID', how='outer')   # Full outer join

# Concat (alt alta veya yan yana ekleme)
pd.concat([df1, df2], axis=0)  # Alt alta (satır)
pd.concat([df1, df2], axis=1)  # Yan yana (sütun)

# Apply fonksiyonu (her satır/sütuna fonksiyon uygula)
df['Maaş_Artış'] = df['Maaş'].apply(lambda x: x * 1.1)

# Map fonksiyonu (değer eşleme)
cinsiyet_map = {1: 'Erkek', 2: 'Kadın'}
df['Cinsiyet'] = df['Cinsiyet_Kod'].map(cinsiyet_map)

# Replace (değer değiştirme)
df['Şehir'].replace('İstanbul', 'İST', inplace=True)

# Query (SQL benzeri sorgulama)
df.query('Yaş > 28 and Maaş > 5000')

# Sample (rastgele örnekleme)
df.sample(5)        # 5 rastgele satır
df.sample(frac=0.1) # %10 rastgele örnek

# Tarih işlemleri
df['Tarih'] = pd.to_datetime(df['Tarih'])
df['Yıl'] = df['Tarih'].dt.year
df['Ay'] = df['Tarih'].dt.month
df['Gün'] = df['Tarih'].dt.day

