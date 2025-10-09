kelime = "galaxy"

# Pozitif indeksler (soldan)
# g  a  l  a  x  y
# 0  1  2  3  4  5

# Negatif indeksler (sağdan)
# g  a  l  a  x  y
#-6 -5 -4 -3 -2 -1

word = "galaxy"

# Pozitif indeks
print(word[0])   # 'g' (ilk karakter)
print(word[5])   # 'y' (son karakter)

# Negatif indeks
print(word[-1])  # 'y' (son karakter)
print(word[-2])  # 'x' (sondan 2.)
print(word[-6])  # 'g' (sondan 6., yani ilk karakter)


# word[-1] her zaman son karakter
# word[-2] her zaman sondan ikinci karakter
# Negatif indeks sağdan saymaya başlar


# Slicing (Dilimleme)

word = "galaxy"

print(word[0:3])   # 'gal' (indeks 0,1,2)
print(word[2:5])   # 'lax' (indeks 2,3,4)
print(word[3:6])   # 'axy' (indeks 3,4,5)


# Negatif İndeksle Slicing

word = "galaxy"

# Sondan dilimleme
print(word[-2:])   # 'xy' (son 2 karakter)
print(word[-3:])   # 'axy' (son 3 karakter)
print(word[-4:])   # 'laxy' (son 4 karakter)



# Baştan Kesme (Sondakileri Atma)

word = "galaxy"

# Sondan N karakteri atma
print(word[:-1])   # 'galax' (son 1 hariç)
print(word[:-2])   # 'gala' (son 2 hariç)
print(word[:-3])   # 'gal' (son 3 hariç)


# Karışık Örnek

kelime = "merhaba"

# Pozitif + Negatif karışık
print(kelime[2:-2])   # 'rha' (indeks 2'den sondan 2. karaktere kadar)
print(kelime[1:-1])   # 'erhab' (ilk ve son karakter hariç)
print(kelime[-5:-2])  # 'rha' (sondan 5. ile sondan 2. arası)


# Tersine Çevirme

kelime = "dünya"

# Tüm stringi tersine çevir
print(kelime[::-1])   # 'aynüd'
# [::-1] = baştan sona, -1 adımla (geriye doğru)


url = "https://example.com/page"

# Parçaları ayır
print(url[0:8])    # 'https://' - protokol

print(url[8:-5])   # 'example.com' - domain    Başlangıç: indeks 8 → 'e' karakteri (example'ın 'e'si)  Bitiş: indeks -5 → '/' karakteri (hariç!)

print(url[-5:])    # '/page' - sayfa yolu


# Alternatif yöntem

url = "https://example.com/page"

# Daha iyi yöntem
# Protokolü at
domain_with_path = url.split("://")[1]  # 'example.com/page'

# İlk / işaretine kadar al
domain = domain_with_path.split("/")[0]  # 'example.com'


