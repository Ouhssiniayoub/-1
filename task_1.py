name = input("Укажите свое имя: "))
if name == "Иван":
    print("Ваше имя не подходит")
age = int(input("Укажите свой возраст: "))
if age >= 16 and age < 75 :
    print("Поздравляем вы поступили в ВГУИТ")
elif age < 16 and age > 0 :
    print("Сначала нужно окончить школу")
elif age < 16:
    print("Вам осталось учиться в школе ",16-age,)
else:
    print("Введите возраст корректно")


