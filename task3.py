# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

from math import factorial
def combination (x,y):
    return int(factorial(x)/(factorial(y)*factorial(x-y)))
m=combination(9,3)
n=combination(15,3)
p=m/n
print(p)