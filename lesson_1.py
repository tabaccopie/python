# 1
one = 1
two = 2
print(one, two)
a = input('Введите число: ')
print(a)
name = input("Введите Ваше имя: ")
print('Привет, %s!' % name)

# 2
seconds = int(input('Введите число секунд: '))
if seconds <= 0:
    print("Число должно быть больше нуля!")
else:
    minutes = seconds // 60
    seconds = minutes % 60
    hours = minutes // 60
    minutes = minutes % 60
    print(f"Время {hours:02d}:{minutes:02d}:{seconds:02d}")

# 3
n = input("Введите число n: ")
summ = int(n) + int(n*2) + int(n*3)
print("Сумма n + nn + nnn равна: ", summ)

#4
num = list(input('Введите целое положительное число: '))
i = 0
mnum = 0
while i < len(num)-1:
    if int(mnum) < int(num[i+1]):
        mnum = int(num[i+1])
    else:
        mnum = int(num[i])
    i += 1
print("Максимальная цифра в числе: %s" % mnum)


#5
debt = int(input('Введите выручку: '))
cred = int(input('Введите издержки: '))
if debt <= cred:
    print('Вы работаете в убыток :(')
else:
    print('У вас есть прибыль! :)')
    print('Рентабельность %s' % ((debt-cred)/debt))
    empl = int(input('Введите количество сотрудников: '))
    if empl <= 0:
        print("Число сотрудников должно быть больше нуля!")
    else:
        print("Прибыль на одного сотрудника составила %s" % ((debt-cred)/empl))


#6
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
if b <= a:
    print('Число b должно быть больше числа a!')
else:
    day = 1
    while a <= b:
        a = a/10 + a
        day += 1
    print('%s' % day)
