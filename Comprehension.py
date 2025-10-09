# Comprehnesion

# Python comprehensions, Python'da liste, dictionary, set ve generator gibi veri yapılarını kısa ve okunabilir bir şekilde oluşturmak için kullanılan güçlü bir özelliktir.

# List comprehension

salaries = [1000,2000,3000,4000,5000]

def new_salary(x):
  return x * 20 / 100 + x

 # tek başına if kullanıyorsak en sağda olur. Else ile beraber kullanılacaksa for en sağda olur
print([new_salary(salary*2) if salary < 3000 else new_salary(salary) for salary in salaries])

students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

print([student.lower() if student in students_no else student.upper() for student in students])


# Dictionary Comprehension

dictionary = {"a":1,
              "b":2,
              "c":3}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())

print({k: v**2 for k, v in dictionary.items()})
print({k.upper(): v**2 for k, v in dictionary.items()})

# Amaç : çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# Key'ler orjinak değerler value'ler ise değiştirilmiş değerler olacak.

numbers = range(10)
new_dict={}

for n in numbers:
    if n % 2 == 0:
        a = new_dict[n] = n ** 2
print(new_dict)

#List Comprehension ile
{n: n ** 2 for n in numbers if n % 2 == 0}
