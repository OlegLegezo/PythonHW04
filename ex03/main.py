# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import os

path = os.path.join('PythonHW04', 'ex03', 'fileinput.txt')
with open(path, 'r') as f:
    text = f.readline()

# метод для конвертации в инт из строку


def convert_to_int(str):
    return [int(x) for x in str.split()]


int_list = convert_to_int(text)
print(int_list)


newArr = []
for el in int_list:
    if int_list.count(el) == 1:
        newArr.append(el)
print(f'неповторяющиеся элементы: {newArr}')


# мысли вслух:
# тут задумывал сделать список повторных элементов
# arrTemp = []
# # answerArr = int_list.copy()

# for j in range(int(len(int_list))):
#     for i in range(int(len(int_list))):
#         if j != i and int_list[j] == int_list[i]:
#             arrTemp.append(int_list[j])
#             print(arrTemp)
#             break


# print(arrTemp)


# a={1, 2, 7, 1, 6, 7, 8, 1}
# b={1,7,1,7,1}
# df=a.difference(b)
# print(df)

'''
тут выбор элементов уникальных set-ом
def uniqueArr(arr):
    list_of_unique_arr = []
    uniqueArr = set(arr)

    for number in uniqueArr:
        list_of_unique_arr.append(number)

    return list_of_unique_arr

print(uniqueArr(int_list))
'''
