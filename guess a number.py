import random
import time
number = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку. Я загадал определенное число")
time.sleep(0.5)
print("Сможете ли Вы его угадать?")
while True:
    time.sleep(0.5)
    print("Введите Вашу догадку: ")
    user_number = int(input())
    if user_number > number:
        print("Слишком много, попробуйте еще раз!")
    elif user_number < number:
        print("Слишком мало, попробуйте еще раз!")
    if user_number == number:
        print("Вы угадали, поздравляем!")
        print("Хотите сыграть еще раз?")
        break
