import pytest

from src.life.core.game_v2 import Life


@pytest.mark.parametrize(
    'cell, result',
    [
        [(24, 24), {(24, 25), (25, 25), (25, 24), (25, 23), (24, 23), (23, 23), (23, 24), (23, 25)}],
        [(0, 0), {(0, 1), (1, 1), (1, 0), (1, 49), (0, 49), (49, 49), (49, 0), (49, 1)}],
        [(0, 49), {(0, 0), (1, 0), (1, 49), (1, 48), (0, 48), (49, 48), (49, 49), (49, 0)}],
        [(49, 49), {(49, 0), (0, 0), (0, 49), (0, 48), (49, 48), (48, 48), (48, 49), (48, 0)}],
        [(49, 0), {(49, 1), (0, 1), (0, 0), (0, 49), (49, 49), (48, 49), (48, 0), (48, 1)}],
    ]
)
def test_get_neighbours(life, cell, result):
    neighbors = life._get_neighbours(cell)
    assert neighbors == result


@pytest.mark.parametrize(
    'start_state, expected',
    [
        [{(24, 23), (24, 24), (24, 25)}, {(23, 24), (24, 24), (25, 24)}],
        [{(23, 23), (23, 24), (24, 23), (24, 24)}, {(23, 23), (23, 24), (24, 23), (24, 24)}],
    ]
)
def test_calc_generation(life, start_state, expected):
    life = Life(first_generation=start_state)
    new_generation = life._calc_new_generation()
    assert new_generation == expected
