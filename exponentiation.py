
n = int(input("Введите количество элементов: "))

numbers = []

for _ in range(n):
    element = input("Введите элемент: ")
   
    try:
        element = int(element)
    except ValueError:
        pass
    numbers.append(element)

power = int(input("Введите степень: "))


result = []
for item in numbers:
    if isinstance(item, int):
        result.append(item ** power)
    elif isinstance(item, str):
        result.append(item * power)
    else:
  
        result.append(item ** power)

print("Результат:", result)
