list = [i ** 2 for i in range(0, 20)]
print(list)

list1 = [i % 3 for i in list]
print(list1)


list2 = [1, 'd', 3, 'g', 'qwe', 2342, 0]
list3 = [item for item in list2 if type(item) == int]
print(list3)
