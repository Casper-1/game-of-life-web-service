from src.life.core.game_v1 import init_game
from src.life.core.utils import loop_field


class Life:
    def __init__(self, first_generation: set):
        self.state = first_generation
        self._all_uniq_generations = set()
        self._cash = None

    def get_next_generation(self):
        """Метод получения следующего поколения. Если первая итерация, вернет первое поколение"""
        if not self._cash:
            self._cash = 1
            return self.state

        new_generation = self._calc_new_generation()
        if new_generation == self.state or new_generation in self._all_uniq_generations:
            return {'msg': 'game over'}

        self.state = new_generation
        self._all_uniq_generations.add(frozenset(new_generation))

        return new_generation

    def _calc_new_generation(self):
        """Метод расчета следующего поколения."""
        new_generation = set()
        self._cash = set()
        for cell in self.state:
            self._cash.add(cell)
            neighbours = self._get_neighbours(cell)
            alive_neighbors = self._calc_alive_neighbours_count(neighbours, self.state)
            if alive_neighbors == 2 or alive_neighbors == 3:
                new_generation.add(cell)
            new_life = self._calc_newborn_cells(neighbours, self.state)
            new_generation.update(new_life)
        return new_generation

    def _get_neighbours(self, cell: tuple) -> set:
        x, y = cell
        incr = range(-1, 2)
        neighbours = {loop_field((x + i, y + j)) for i in incr for j in incr if not (i == 0 and j == 0)}
        return neighbours

    def _calc_alive_neighbours_count(self, neighbours: set, generation: set) -> int:
        """Функция подсчета количества живых соседних клеток"""
        alive_neighbours = neighbours & generation
        return len(alive_neighbours)

    def _calc_newborn_cells(self, neighbours: set, generation: set) -> set:
        """Функция определения клеток, в которых зародится жизнь"""
        new_life = set()
        for cell in neighbours:
            if cell in self._cash or cell in self.state:
                continue
            neighbours_neighbours = self._get_neighbours(cell)
            self._cash.add(cell)
            alive_cells_count = self._calc_alive_neighbours_count(neighbours_neighbours, generation)
            if alive_cells_count == 3:
                new_life.add(cell)
        return new_life


first_generation = init_game()
life = Life(first_generation=first_generation)
