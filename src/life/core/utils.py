import random

from src.life.core.constants import MAX_X, MAX_Y


def init_game():
    return {(random.randint(25, 35), random.randint(25, 35)) for i in range(50)}


def loop_field(cell: tuple) -> tuple:
    """Функция зацикливания игрового поля"""
    x, y = cell
    if x < 0:
        x = x + MAX_X
    if y < 0:
        y = y + MAX_Y
    if x >= MAX_X:
        x = x - MAX_X
    if y >= MAX_Y:
        y = y - MAX_Y
    return x, y
