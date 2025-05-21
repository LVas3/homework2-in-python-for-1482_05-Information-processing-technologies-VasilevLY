
list1 = list(map(int, input("Введите первый список: ").split()))

list2 = list(map(int, input("Введите второй список: ").split()))

set1 = set(list1)
set2 = set(list2)

common_elements = set1.intersection(set2)

print("Общие элементы:", *common_elements)
