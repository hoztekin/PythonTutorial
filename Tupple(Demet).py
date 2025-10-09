# Değiştirilemez
# Sıralıdır
# Kapsayıcıdır

t = ("John", "Doe",3, True, 80)

t[0:3] # => Slice 0'dan 3'e kadar

t[0] = 20    # Değiştirilemez Tupple ın en önemli özelliği

# İllaki değerlerini değiştireceğim diyorsan
# Öncel list e cast et sonra değeri değiştir
# Sonra tekrar tupple a cast et