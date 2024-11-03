my_dict = {'Timofey': 1989, 'Arseniy': 1992}
print (my_dict)
print (my_dict['Timofey'])
print (my_dict.get('Matvey'))
my_dict.update({'Max': 1995, 'Taisa': 1990})
a = my_dict.pop('Arseniy')
print (a)
print (my_dict)

my_set = {23, 'Stone', True, 'Stone', 23, 23, 5.6}
print (my_set)
my_set.add(('Potato', 54))
print(my_set.remove(23))
print (my_set)
