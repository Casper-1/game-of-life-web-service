import pytest

from src.life.core.game_v1 import calc_generation, get_neighbours


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
def test_get_neighbours(cell, result):
    neighbors = get_neighbours(cell)
    assert neighbors == result


@pytest.mark.parametrize(
    'start_state, expected',
    [
        [{(24, 23), (24, 24), (24, 25)}, {(23, 24), (24, 24), (25, 24)}],
        [{(23, 23), (23, 24), (24, 23), (24, 24)}, {(23, 23), (23, 24), (24, 23), (24, 24)}],
    ]
)
def test_calc_generation(start_state, expected):
    new_generation = calc_generation(start_state)
    assert new_generation == expected
