"""Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделенных пробелами. Программа
должна подсчитывать сумму чисел в
файле и выводить ее на экран."""

with open("user_nums.txt", "w",
                    encoding="utf-8") as f_obj:
    user_line = input("Введите числа, "
                    "разделенные пробелами: ")
    f_obj.writelines(user_line)
    my_line = user_line.split()

    print(f"Сумма Ваших чисел равна"
          f" {sum(map(int, my_line))}")
