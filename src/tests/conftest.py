import pytest

from src.life.core.game_v2 import Life
from src.life.core.utils import init_game


@pytest.fixture(scope="function")
def life():
    start_state = init_game()
    return Life(first_generation=start_state)
