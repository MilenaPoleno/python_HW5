"""Создать текстовый файл (не
программно), сохранить в нем несколько
строк, выполнить подсчет количества
строк, количества слов в каждой
строке."""

with open("test.txt", encoding="utf-8") \
        as data_file:
    for num, line in \
            enumerate(data_file.readlines()):
        num += 1
        print(f"В строке {num} {len(line.split())}"
                f" слов(о)")
    print(f"Всего строк в файле {num}")
