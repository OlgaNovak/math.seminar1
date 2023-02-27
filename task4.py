# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

from math import factorial
def combination (x,y):
    return int(factorial(x)/(factorial(y)*factorial(x-y)))
m=combination(2,2)
n=combination(100,2)
p=m/n
print(p)