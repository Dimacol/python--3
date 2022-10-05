
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

myList = [2, 3, 5, 9, 3]
print("Мой список:")
print(myList)
list_length=len(myList)
sumElements=0
for i in range(list_length):
    if i % 2 != 0:
        sumElements += myList[i]
print("Сумма элементов на нечетных позициях:", sumElements)