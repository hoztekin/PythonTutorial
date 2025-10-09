# Sözlük (Dictionary)

# Değiştirilebilir.
# Sırasızdır
# Kapsayıcıdır

#Key valeu çifti

dictionary = {"Reg": "Regression",
              "Log": "Logictic Regression"}

dictionary["Reg"]

dictionary = {"Reg": ["Regression", 20],
              "Log": ["Logictic Regression", False, 80]}

dictionary["Reg"]

dictionary["Log"][2]

dir(dictionary)

dictionary.keys()

dictionary.values()

dictionary.items()  # Tupple formatına çevirir key value olarak

dictionary.update({"LR" : False}) # Update de güncelleme yapar ancak ilgili key değeri yoksa en sona oluşturur.

