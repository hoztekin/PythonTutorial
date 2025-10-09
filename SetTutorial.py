# Değiştirilebilir
# Sırasız + Eşsizdir
# Kapsayıcıdr.

# Hız gerektiren işlemlerde kullanılabilir

set1 = set([1, 2, 3])
set3 = set([1, 2, 5])
set2 = set(["a", True, 40.30])

set1.difference(set2) #set1 de olup set2 de olmayanlar

set1.symmetric_difference(set2) #Simetrik olarak kümelerde (İki kümede de) olmayanları getirir

set1.intersection(set3) #Kesişenleri getirir

set1.union(set3) #Birleştirme

set1.isdisjoint(set2)  #İki kümenin kesişimi boş mu? True False döner


setP = set([1,2,3])     # Bir küme diğer kümenin alt kümesi mi?
setC = set([1,2,3,5])

setP.issubset(setC)
setC.issubset(setP)

# Issuperset => Bir küme diğer kümeyi kapsıyor mu?

setC.issuperset(setP)


def kume_analizi(set1, set3):
    if set1.issuperset(set3):
        return set1.intersection(set3)
    else:
        return set3.difference(set1)

sonuc = kume_analizi(set1, set3)
print("Sonuç:", sonuc)