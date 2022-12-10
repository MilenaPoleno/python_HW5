"""Создать программно файл в текстовом
формате, записать в него построчно
данные, вводимые пользователем. Об
окончании ввода данных
свидетельствует пустая строка."""

with open("user_data.txt", "w",
                    encoding="utf-8") as f_obj:
    user_line = input("Введите данные: ")
    while user_line:
        f_obj.writelines(f"{user_line} \n")
        user_line = input("Введите данные: ")
        if not user_line:
            break

with open("user_data.txt", 'r',
                    encoding="utf-8") as f_obj:
    print(f_obj.readlines())
