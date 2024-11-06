grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades [0] = sum(grades [0]) / len(grades [0])
grades [1] = sum(grades [1]) / len(grades [1])
grades [2] = sum(grades [2]) / len(grades [2])
grades [3] = sum(grades [3]) / len(grades [3])
grades [-1] = sum(grades [-1]) / len(grades [-1])
a = dict.fromkeys(students, 0)
a.update({'Johnny' : grades [2], 'Bilbo':grades [1],'Steve':grades [-1],'Khendrik':grades[3],
            'Aaron':grades [0]})
b = input('Введите имя ученика: ')
print('Его средний балл: ', a.setdefault(b))