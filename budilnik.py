import time
import pyglet

while True:
    a = str(input("Желаите создать будильник?(да)/(нет): "))
    print()
    if a == str("Нет") or a == str("нет"):
        print("Хорошо, работа окончена.")
        break
        print()
    if a == str("Да") or a == str("да"):
        b = str(input("Введите название текст, который будет выводится при работе будильника: "))
        print()
        hour = int(input("Введите на сколько часов хотите поставить будильник: "))
        print()
        min = int(input("Введите на сколько минут хотите поставить будильник: "))
        print()
        print("Будильник был устоновлен на ", hour, ":", min)
        print()

        i = True
        while True:
            tim = str(time.strftime("%H:%M:%S", time.localtime()))
            if tim[:5] == f'{hour}:{min}' and i:
                i = False
                sound = pyglet.media.load('Мелодия 1.mp3', streaming=True)
                sound.play()
                print(b)
            time.sleep(1)
