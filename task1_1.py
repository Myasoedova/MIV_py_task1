# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран
a = 5
b = 2
c = a ** b
d = 'Ivanov'
e = 200.15
man = ['Misha', 'Kolya', d]
numbers = (a, b, c, e)
f = True
print(a)
print(b)
print(c)
print(d)
print(e)
print(type(a))
print(type(e))
print(type(numbers))
print(man)
print(man[-2])
print(100+5)
print(100+int(float('2.3')))
name = input('Как вас зовут?')
print('Привет,', name)
age = input('Сколько Вам лет?')
print('Если вы М, выход на пенсию через, ', 65-int(age))
print('Если вы Ж, выход на пенсию через, ', 63-int(age))
# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
print('********************* задача 2********************')
numb = input('Введите число: ')
print('Результат сложения вашего числа и 2:  ', 2+int(numb))

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
print('********************* задача 3********************')
user_age = int(input('Укажите ваш возраст: '))
if user_age >= 18:
    print('Доступ разрешен!')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')