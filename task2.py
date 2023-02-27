# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

from math import factorial
def combination (x,y):
    return int(factorial(x)/(factorial(y)*factorial(x-y)))
m=combination(3,3)
n=combination(10,3)
p=m/n
print(p)