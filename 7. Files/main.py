import os
from pprint import pprint

def get_files():
    path = '/Users/dimitriy/Developers/netology/myhomework-netology/7. Files/files'
    count_rows = {}
    count_rows_sort = []
    directory = [files for files in os.listdir(path) if files.endswith('.txt')]
    for file in directory:
        with open(os.path.join(path, file), 'rt', encoding='utf-8') as f:
            count_rows[file] = len(f.readlines())
    count_rows_sort = sorted(count_rows, key = count_rows.get)
    for file in count_rows_sort:
        with open('out.txt', 'a', encoding='utf-8') as new_f:
            with open(os.path.join(path, file), 'rt', encoding='utf-8') as f:
                new_f.write(file + '\n')
                new_f.write(str(count_rows.get(file)) + '\n')
                new_f.write(''.join(f.readlines()) + '\n')
    return 'Откройте файл out.txt'

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = make_cook_book('recipes.txt')
    shop_list = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            ingredient_name, quantity, measure = ingredients.values()
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += int(quantity) * person_count
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': int(quantity) * person_count}
    return shop_list


def make_cook_book(filename):
    path = '/Users/dimitriy/Developers/netology/myhomework-netology/7. Files/recipes.txt'
    cook_book = {}
    with open(path, 'rt', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            ing_count = int(file.readline())
            ingridients = []
            for ing in range(ing_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingridients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book[dish_name] = ingridients
    return cook_book

def main():
    #print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    get_files()

if __name__ == "__main__":
    main()