first = int(input('Введите число: '))
second = int(input('Следующее: '))
third = int(input('И последнее: '))
if first == second or first == third or second == third:
    print (2)
elif first == second == third:
    print (3)
elif first != second != third:
    print (0)