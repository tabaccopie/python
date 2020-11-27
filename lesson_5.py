# 1. + Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.
with open("lesson_5-1-2.txt", "w") as my_file:
    my_str = " "
    while my_str:
        my_str = input("Введите строку для записи, для выхода оставьте пустую строку и нажмите Enter: ")
        my_file.write(my_str + "\n")


# 2. + Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
str_num = 0
w_num = 0
with open("lesson_5-1-2.txt", "r") as my_file:
    for line in my_file:
        if line != "\n":
            str_num += 1
            w_line = line.split()
            w_num = w_num + len(w_line)

print(f"Количество строк в файле: {str_num}")
print(f"Количество слов в файле: {w_num}")

# 3. + Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
my_count = 0
my_sum = 0
with open("lesson_5-3.txt", "r") as my_file:
    print("Получающие менее 20000: ")
    for line in my_file:
        my_count += 1
        my_list = line.split()
        if int(my_list[1]) < 20000:
            print(my_list[0])
        my_sum += int(my_list[1])

print(f"Средняя заработная плата: {my_sum / my_count}")


# 4. + Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Необходимо
# написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
my_dict1 = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file_in = open("lesson_5-4-1.txt", "r")
file_out = open("lesson_5-4-2.txt", "w")

for line in file_in:
    tmp_number = line.partition(" ")
    file_out.write(line.replace(tmp_number[0], my_dict1[tmp_number[0]]))

file_out.close()
file_in.close()


# 5. + Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.
try:
    with open("lesson_5-5.txt", "w+") as my_file:
        my_file.write("34 6 23 87 392 74 22 46")
        my_file.seek(0)
        my_num = sum(map(int, my_file.readline().split()))
except IOError as err:
    print(err)

print(f"Сумма чисел: {my_num}")

# 6. + Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран. Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
#
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
try:
    with open("lesson_5-6.txt", "r") as my_file:
        my_dict = {}
        for line in my_file:
            my_list_tmp = line.split()
            my_list = list(filter(lambda x: x.isdigit() or x == ' ', line))
            my_str = "".join(my_list)
            my_sum = sum(map(int, my_str.split()))
            print(my_sum)
            my_dict[my_list_tmp[0]] = my_sum
except IOError as err:
    print(err)

print(my_dict)

# 7. + Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать
# файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением
# убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]. Итоговый
# список сохранить в виде json-объекта в соответствующий файл. Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json

my_dict1 = {}
my_dict2 = {}

try:
    with open("lesson_5-7.txt", "r") as my_file:
        count = 0
        av_profit = 0
        for line in my_file:
            my_list_tmp = line.split()
            profit = int(my_list_tmp[2]) - int(my_list_tmp[3])
            my_dict1[my_list_tmp[0]] = profit
            if profit > 0:
                count += 1
                av_profit += profit

except IOError as err:
    print(err)

my_dict2["average_profit"] = av_profit
my_list = [my_dict1, my_dict2]
try:
    with open("lesson_5-7.json", "w") as my_file_json:
        json.dump(my_list, my_file_json)

except IOError as err1:
    print(err1)
