# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
from random import randint as rnd
k = int(input('Задайте натуральную степень:'))


inputArr = str()
inputArr = [rnd(0, 100) for _ in range(k+1)]
print(inputArr)


res1 = ""
for i in range(int(len(inputArr))):
    needPlus = 0
    if inputArr[i] > 0 and i != int(len(inputArr)-1) and i != int(len(inputArr)-2):
        res1 += f'{inputArr[i]}x^{len(inputArr)-1-i}'
        needPlus = 1
    if inputArr[i] > 0 and i == int(len(inputArr)-2):
        res1 += f'{inputArr[i]}x'
        needPlus = 1
    if inputArr[i] > 0 and i == int(len(inputArr)-1):
        res1 += f'{inputArr[i]}=0 '
    if inputArr[i] <= 0 and i == int(len(inputArr)-1):
        res1 += f'=0 '
    if needPlus == 1:
        res1 += f'+'
        needPlus = 0

print(res1)


path = os.path.join('PythonHW04', 'ex04', 'file.txt')

with open(path, 'a') as f:
    f.write(res1+"\n")


'''
решение одногруппника

k = int(input('Please enter a k-degree: '))
signs = ['+', '-']
coefficients = []
for _ in range(k + 1):
    coefficients.append(rnd(0,10))
result = ''
for i in range(k, 0, -1):
    if i == 1:
        result += f'{coefficients[i]}*x^{i} {signs[rnd(0,1)]} {coefficients[0]} = 0'
    else:
        if coefficients[i] != 0:
            result += f'{coefficients[i]}*x^{i} {signs[rnd(0,1)]} '
with open('polynoms.txt', 'a') as file:
    file.write(result + "\n")
print(result)
'''
