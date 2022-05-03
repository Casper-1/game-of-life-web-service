from src.life.core.constants import GAME_OVER
from src.life.core.utils import init_game, loop_field


def get_neighbours(cell: tuple) -> set:
    """Функция получения сех соседей клетки"""
    x, y = cell
    incr = range(-1, 2)
    neighbours = {loop_field((x+i, y+j)) for i in incr for j in incr if not (i == 0 and j == 0)}
    return neighbours


def calc_alive_neighbours_count(neighbours: set, generation: set) -> int:
    """Функция подсчета количества живых соседних клеток"""
    alive_neighbours = neighbours & generation
    return len(alive_neighbours)


def calc_newborn_cells(neighbours: set, generation: set, cash: set) -> set:
    """
    Функция определения клеток, в которых зародится жизнь
    """
    new_life = set()
    for cell in neighbours:
        if cell in cash or cell in generation:
            continue
        neighbours_neighbours = get_neighbours(cell)
        cash.add(cell)
        alive_cells_count = calc_alive_neighbours_count(neighbours_neighbours, generation)
        if alive_cells_count == 3:
            new_life.add(cell)
    return new_life


def calc_generation(current_generation: set) -> set:
    """Функция расчета следующего поколения"""
    new_generation = set()
    cash = set()
    for cell in current_generation:
        neighbours = get_neighbours(cell)
        cash.add(cell)
        alive_neighbors = calc_alive_neighbours_count(neighbours, current_generation)
        if alive_neighbors == 2 or alive_neighbors == 3:
            new_generation.add(cell)
        new_life = calc_newborn_cells(neighbours, current_generation, cash)
        new_generation.update(new_life)
    return new_generation


def main():
    state = init_game()
    all_uniq_generations = set()
    while state:
        yield state
        new_generation = calc_generation(state)
        if new_generation == state or state in all_uniq_generations:
            break
        all_uniq_generations.add(frozenset(state))
        state = new_generation


life = main()


def get_next_generation():
    try:
        new_generation = next(life)
    except StopIteration:
        new_generation = GAME_OVER
    return new_generation
