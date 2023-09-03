from pprint import pprint
import re
from re import match
import csv

path_csv = '/Users/dimitriy/Developers/netology/myhomework-netology/13. Professional work with Python/2. Regexp/phonebook_raw.csv'
with open(path_csv) as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

pattern = re.compile(r"(\+7|8)?\s?\(?(\d{3})\)?\s?-?(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})(.+доб.+(\d{4}))?")

filtred_values = [item for sublist in contacts_list for item in sublist if pattern.match(item)]

for values in filtred_values:
  pprint(values)

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')

## Вместо contacts_list подставьте свой список:
  datawriter.writerows(contacts_list)