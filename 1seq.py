elements_number = int(input('Введите количество элементов: '))
user_list = []
for i in range(elements_number):
    user_elements = int(input(f'Введите {i+1} элемент: '))
    user_list.append(user_elements)
user_list.sort()
print(user_list)