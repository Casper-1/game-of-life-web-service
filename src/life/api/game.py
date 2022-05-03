from typing import Tuple, Set, Union

from fastapi import APIRouter

from src.life.core.game_v1 import get_next_generation
from src.life.core.game_v2 import life

router = APIRouter(
    prefix='/game',
)


@router.get('/v1', response_model=Set[Tuple[int, int]])
def get_state():
    res = get_next_generation()
    return res


@router.get('/v2', response_model=Union[Set[Tuple[int, int]], dict])
def get_state():
    return life.get_next_generation()

