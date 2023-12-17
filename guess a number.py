import random
import time
number = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку. Я загадал определенное число от 1 до 100 включительно.")
time.sleep(0.5)
print("Сможете ли Вы его угадать?")
def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100

def input_number():
    while True:
        time.sleep(0.5)
        user_number = input("Введите Вашу догадку от 1 до 100 включительно: ")
        if is_valid(user_number) == True:
            return int(user_number)
        else:
            print("Чтобы сыграть в игру, Вы должны ввести число, а не", user_number)
            continue

def compare_num():
    counter = 0
    while True:
        user_number = input_number()
        if user_number > number:
            print("Слишком много, попробуйте еще раз!")
            counter += 1
            continue
        elif user_number < number:
            print("Слишком мало, попробуйте еще раз!")
            counter += 1
            continue
        else:
            print("Вы угадали, поздравляем!")
            time.sleep(1)
            print("Суммарное число попыток, за которое Вы смогли отгадать число, равно ", counter, ".", sep = "")
            break
compare_num()

bye_message = input("Спасибо, что играли в числовую угадайку. Хотите сыграть снова? Ответьте только 'да' или 'нет'.\n")
if bye_message.lower() == "да":
    compare_num()
else:
    print("До скорого! Было приятно провести с Вами время:)")
