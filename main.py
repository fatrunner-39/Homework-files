import os
from pprint import pprint


# Задания 1, 2

def recipes_dict(file_name):
    result = dict()

    with open(file_name, encoding='UTF-8') as file:
        for line in file:
            dish = line.strip()
            ingridients_quantity = int(file.readline())
            ingridients_list = []
            for ingridients in range(ingridients_quantity):
                title, quantity, type = file.readline().split('|')
                ingridients_list.append(
                    {'ingredient_name': title, 'quantity': int(quantity), 'measure': type.strip()}
                )
            result[dish] = ingridients_list
            file.readline()

    return result

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = recipes_dict('recipes.txt')
    products = dict()

    for dish in dishes:
        if dish in cook_book.keys():
            for prod in cook_book[dish]:
                {'quantity': prod['quantity'], 'measure': prod['measure']}
                products[prod['ingredient_name']] = {'quantity': prod['quantity'] * person_count, 'measure': prod['measure']}
        else:
            products[dish] = 'Нет рецепта'

    return products

# pprint(get_shop_list_by_dishes(['Шаверма', 'Шашлык', 'Омлет'], 2))
# pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 2))


# Задание 3
# print(os.getcwd())
def pages(directory):
    files_list = os.listdir(path=directory)
    dict_files = dict()
    sorted_dict_files = dict()
    list_lines = []
    for doc in files_list:
        with open(os.path.join(directory, doc), encoding='UTF-8') as file:
            lines = file.read().splitlines()
            list_lines.append(len(lines))
        dict_files[doc] = (len(lines), lines)

    sorted_keys = sorted(dict_files, key=dict_files.get)
    for key in sorted_keys:
        sorted_dict_files[key] = dict_files[key]

    with open('new_file.txt', 'w', encoding='UTF-8') as document:
        for key, val in sorted_dict_files.items():
            document.write(key + '\n')
            document.write(str(val[0]) + '\n')
            for string in val[1]:
                document.write(string + '\n')

folder = os.path.dirname(r'C:\Users\alexa_000\PycharmProjects\homework_files\files\1.txt')
pages(folder)
