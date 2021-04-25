import numpy as np


def score_game(game_core):
    count_list = [] # в этой переменной храним кол-ва попыток-угадываний
    # RANDOM SEED с ненулевым параметром позволяет генерить каждый раз разные "случайные" числа
    np.random.seed(1)
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_list.append(game_core(number))
    # считаем среднее кол-во попыток
    score = int(np.mean(count_list))
    return score


def game_core(number):
    # Функция принимает загаданное число и возвращает число попыток
    count = 1  # cчетчик попыток
    predict = np.random.randint(1, 101)  # попытка угадать число с помощью генератора случайных чисел
    previous_predict = predict  # здесь сохраняем число-попытку для избежания зацикливания
    while True:
        if number == predict:
            # если угадали число, то выходим из цикла
            break
        elif number > predict:
            # если назвали меньшее число, то следующее число-попытка - это среднее между загаданным и числом-попыткой
            # для уменьшения числа попыток
            predict = round(np.mean([predict, number]))
            # если среднее равно предудщей попытке, то просто берем следующее число по возрастанию
            if predict == previous_predict:
                predict += 1
            else:
                # иначе сохраняем новое число-попытку для избежания зацикливания
                previous_predict = predict
        else:
            # если назвали меньшее число, то следующее число-попытка - это среднее между загаданным и числом-попыткой
            predict = round(np.mean([predict, number]))
            # если среднее равно предудщей попытке, то просто берем следующее число по убыванию
            # для уменьшения числа попыток
            if predict == previous_predict:
                predict -= 1
            else:
                # иначе сохраняем новое число-попытку для избежания зацикливания
                previous_predict = predict
        # увеливаем счетчик попыток
        count += 1
    return count


# запускаем основную функцию с передачей вспомогательной функции в качестве параметра
scores_number = score_game(game_core)
print(f"Ваш алгоритм угадывает число в среднем за {scores_number} попыток")
