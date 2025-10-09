import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head()) # İlk 5 kayıt
print(df.tail()) # Son 5 kayıt
print(df.shape) # Boyut bilgisini verir
print(df.info())
print(df.columns)
print(df.describe().T)  #Transpose T ile hızlı bakış için
print(df["sex"].head())

print(df["sex"].value_counts())
# Object ve category tipi Kategorik değişkendir
# Bool harici numeric değişkenlerdir
# Metotlarda inplace argümanı değişikliği kalıcı hale getirir

