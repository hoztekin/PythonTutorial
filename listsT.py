# Listeler değiştirilebilir
# Sıralıdır. Index işlemleri yapabilir
# Kapsayıcıdır. (Farklı veri tiplerini barındırabilir)

notes = [1,2,3, False, 10.80, "Deneme"]
type(notes)

notes[:4] # 0'dan 4'e kadar slice

notes [3:] # 3'den sonrası


not_nam = ["test", 1, bool, 10.30, [1,5]] #=> Kapsayıcı
not_nam[4][1] = "deneme" # => Listeler değiştirilebilir

dir(notes) # Kullanılabilecek metotları listeler

notes.append(30) # Append sona ekler

notes.insert(2, True)  # Belirlediğimiz index e eleman ekler



