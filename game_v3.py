"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 1 # начальное число попыток = 1, т.к. условие для входа в цикл это уже попытка
    predict_max = 101 #начальное максимальное значение диапазона  для поиска
    predict_min = 0 #  минималное значение диапазона для поиска
    predict = (predict_max + predict_min)//2 # начинаем поиск с середины диапазона
    while number != predict: # пока загаданное число не равно нашему 
        count += 1 # увеличиваем количество попыток на 1
        if number > predict: # если загаданное число больше нашего варианта
            predict_min = predict # сдвигаем минимаьную границу диапазона на наше число         
        elif number < predict: # если загаданное число меньше нашего варианта
            predict_max = predict # сдвигаем максимальную границу на наше число
        predict = (predict_max + predict_min)//2 # число для сравнения ставим в середину текущего диапазона
    # Ваш код заканчивается здесь    
    return count


def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
