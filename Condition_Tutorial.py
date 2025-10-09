1 == 1

if 1 == 1:
    print("eşit")

# if koşulu True ise ilk blok çalışır
# False ise else bloğu çalışır
# İki bloktan sadece biri çalışır

yas = 18

if yas >= 18:
   print("Ehliyet alabilirsiniz")
else:
    print("Ehliyet alamazsınız")



# Koşullar yukarıdan aşağı kontrol edilir
# İlk True olan koşulun bloğu çalışır ve yapı sonlanır
# Hiçbiri True değilse else bloğu çalışır
# elif = "else if" (değilse eğer)

puan = 75

if puan >= 90:
    print("Not: A")
elif puan >= 80:
    print("Not: B")
elif puan >= 70:
    print("Not: C")
elif puan >= 60:
    print("Not: D")
else:
    print("Not: F")


# Bir if bloğunun içinde başka if bloğu olabilir
# İkinci if ancak birinci if True ise kontrol edilir
# Her if'in kendi else'i olabilir

kullanici_adi = "admin"
sifre = "1234"

if kullanici_adi == "admin":
    if sifre == "1234":
        print("Giriş başarılı")
    else:
        print("Şifre hatalı")
else:
    print("Kullanıcı bulunamadı")


# and: Tüm  koşullar True  olmalı
# or: En  az  bir  koşul   True  olmalı
# not: Koşulu  tersine  çevirir

yas = 25
ehliyet = True
deneyim_yili = 3

if yas >= 21 and ehliyet and deneyim_yili >= 2:
    print("Araç kiralayabilirsiniz")
else:
    print("Araç kiralayamazsınız")


# > büyük
# < küçük
# >= büyük eşit
# <= küçük eşit
# == eşit
# != eşit değil

sayi = 15

if sayi > 10:
    print("10'dan büyük")
elif sayi == 10:
    print("10'a eşit")
else:
    print("10'dan küçük")


# in operatörü bir elemanın liste/string içinde olup olmadığını kontrol eder
# not in ile tersini kontrol edebilirsiniz

meyve = "elma"
meyveler = ["elma", "armut", "muz"]

if meyve in meyveler:
    print(f"{meyve} listede var")
else:
    print(f"{meyve} listede yok")


# Kısa if-else yapısı (Ternary)
# Format: değer_true if koşul else değer_false
# Değişkene atama için kullanışlı
yas = 20
durum = "Yetişkin" if yas >= 18 else "Çocuk"
print(durum)