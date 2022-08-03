# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import os
path1 = os.path.join('PythonHW04', 'ex05', 'input1.txt')
with open(path1, 'r') as my_file:
    data1 = my_file.read()
data1 = data1.split()
data1 = data1[:-2]
print(data1)

path2 = os.path.join('PythonHW04', 'ex05', 'input2.txt')
with open(path2, 'r') as my_file:
    data2 = my_file.read()
data2 = data2.split()
# data2 = data2.split('x')
data2 = data2[:-2]
print(data2)


# функция поиска x^
def finder(n):
    temp = []
    for i in data1:
        # print(f'i={i}')
        if (f"x^{n}") in i:
            for j in data2:
                # print(f'j={j}')
                if (f"x^{n}") in j:
                    # print('список х^:')
                    temp.append(f"x^{n}")
                    # print(temp)
                    n = n-1
                    # if n>1:
                    #     finder (n)
                    #     print('сработала рекурсия')
    # print(f'список x^:{temp}')
    return (temp)


xArr = finder(4)
print(f'список x^:{xArr}')


xArrSum = []
for m in xArr:
    k = 0
    for i in data1:
        l = 0
        for j in data2:
            if m in i and m in j:
                # print('qwerty')
                # print(k)
                # print(l)
                xArrSum.append(f'{(int(data1[k][:-3])+int(data2[l][:-3]))}{m}')
                xArrSum.append(f'+')
                data1.pop(k)
                data2.pop(l)
                # print(xArrSum2)
            l += 1
        k += 1
print(xArrSum)
# print('data1temp:')
# print(data1)
# print('data2temp:')
# print(data2)

m='x'
k = 0
for i in data1:
    l = 0
    for j in data2:
        if m in i and m in j: 
            xArrSum.append(f'{(int(data1[k][:-1])+int(data2[l][:-1]))}{m}')
            xArrSum.append(f'+')
            data1.pop(k)
            data2.pop(l)            
        l += 1
    k += 1
print(xArrSum)

# print(data1)
# print(data2)


def plusDeletter(data1):
    k=0
    for i in data1:
        if '+' in i:
            data1.pop(k)
            plusDeletter(data1)
        k+=1

plusDeletter(data1)
plusDeletter(data2)
# print(data1)
# print(data2)

xArrSum.append(f'{(int(data1[0])+int(data2[0]))}')
xArrSum.append(f'=0')
print(xArrSum)

path = os.path.join('PythonHW04', 'ex05', 'output.txt')

with open(path, 'a') as f:
    for item in xArrSum:
        f.write("%s" % item)