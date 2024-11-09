my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = my_list [4]
print ('Вы видите список чисел', my_list)
while True:
    b = int(input('Введите число из списка: '))
    if a < len(my_list) and b >= a:
        continue
    else:
        break