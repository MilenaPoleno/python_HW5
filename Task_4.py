"""Создать (не программно) текстовый
файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу,
открывающую файл на чтение и
считывающую построчно данные. При
этом английские числительные должны
заменяться на русские. Новый блок строк
должен записываться в новый текстовый
файл."""

translate = {"One": "Один", "Two": "Два",
             "Three": "Три", "Four": "Четыре"}
new_nums = []

with open("nums.txt", encoding="utf-8") \
        as nums:
    for line in nums:
        line = line.split(' ', 1)
        new_nums.append(f""
                        f"{translate[line[0]]} {line[1]}")

with open("translate.txt", "w",
                    encoding="utf-8") as tr_file:
    tr_file.writelines(new_nums)
