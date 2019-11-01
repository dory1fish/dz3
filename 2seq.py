new_string = input('Введите элементы списка через запятую: ')
if ',' in new_string:
    elements_sep = ','
elif ';' in new_string:
    elements_sep = ';'
elif '/' in new_string:
    elements_sep = '/'
new_string = new_string.split(elements_sep)
new_list = [int(x) for x in new_string]
unique_elements = set(new_list)
unique_list = list(unique_elements)
print(unique_list)