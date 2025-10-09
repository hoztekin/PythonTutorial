# Lambda

new_sum = lambda a, b : a + b

print(new_sum(4,5))

salaries = [1000,2000,3000,4000,5000]


def new_salary(x) :
    return x * 20 / 100 + x


new_salary(2000)

for salary in salaries :
    print(new_salary(salary))

# Map
# Bana bir fonksiyon ver ver bir de liste ver döngü olmadan ben uygulayım

list(map(new_salary, salaries))   # 1. yöntem

list(map(lambda x : x * 20 / 100 + x, salaries))   #2.  yöntem

# Filter

list_store = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x : x % 2 == 0, list_store)))

# Reduce

from functools import reduce

list_store = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y : x + y, list_store))

# Lambda = isimsiz, tek satırlık fonksiyon

kare = lambda x: x ** 2
print(kare(5))  # 25


# Daha fazla parametre:
toplam = lambda x, y: x + y
print(toplam(3, 5))  # 8

uc_sayi = lambda a, b, c: a + b + c
print(uc_sayi(1, 2, 3))  # 6