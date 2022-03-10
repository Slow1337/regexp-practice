from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding="UTF-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
# pattern = re"([А-Я]\w+\b)+(\s|\,)+([А-Я]\w+)+(\s)+([А-Я]\w+)+(,,)"
search_pattern = r"([А-Я]\w+\b)+(\s|\,)+([А-Я]\w+)+(\s)+([А-Я]\w+)+(\,)+"
except_pattern = r"([А-Я]\w+)\s([А-Я]\w+)"
except_sub_pattern = r"\1,\2"
sub_pattern = r"\1,\3,\5,"
comma_pattern = r"(\,{3}|\,{2})+"
comma_sub_pattern = r","
phone_pattern = r"(\+7|8)(\s?)((\(?)(\d{3})(\)?))(\s?|\-?)(\d{3})(\-?)(\d{2})(\-?)(\d{2}(\s?))((\(?)(доб\.)(\s)(\d+)(\)?))?"
phone_sub_pattern = r"+7(\5)\8-\10-\12\16\18"
for id, container_entry in enumerate(contacts_list):
    str_entry = ",".join(container_entry)
    str_entry = re.sub(search_pattern, sub_pattern, str_entry)
    str_entry = re.sub(comma_pattern, comma_sub_pattern, str_entry)
    str_entry = re.sub(except_pattern, except_sub_pattern, str_entry)
    str_entry = re.sub(phone_pattern, phone_sub_pattern, str_entry)
    contacts_list[id] = str_entry.split(sep=",")
for id, container_entry in enumerate(contacts_list):
    if container_entry == contacts_list[0]:
        pass
    lastname = container_entry[0]
    for second_iteration in contacts_list:
        if container_entry == second_iteration:
            pass
        elif container_entry[0] == second_iteration[0]:
            container_entry.extend(second_iteration)
            contacts_list.remove(second_iteration)
            container_entry.reverse()
            for entry in container_entry:
                if container_entry.count(entry) >= 2:
                    container_entry.remove(entry)
                elif entry == '':
                    container_entry.remove(entry)
            container_entry.reverse()
            contacts_list[id] = container_entry
pprint(contacts_list)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)


