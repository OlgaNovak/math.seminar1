# Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, что все карты – крести. 
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

from math import factorial
def combination (x,y):
    return int(factorial(x)/(factorial(y)*factorial(x-y)))
m=combination(13,4)
n=combination(52,4)
p1=m/n
p2=(combination(4,1)*combination(48,3)+combination(4,2)*combination(48,2)+combination(4,3)*combination(48,1)+combination(4,4))/n
print(f'Ответ для а):{p1}')
print(f'Ответ для б):{p2}')
