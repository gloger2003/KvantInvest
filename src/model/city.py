import numpy as np
from typing import List, Optional

from model.enums import BlocksEnum


class CityGrid:
    def __init__(self, N: int = 10, M: int = 10):
        self._height = N
        self._weight = M
        self._matrix = self.create_grid(N, M)

    @staticmethod
    def create_grid(N: int = 10, M: int = 10) -> np.array:
        """ Создаёт сетку (город) """
        block_set = set(k.value for k in BlocksEnum)
        matrix = np.random.randint(
            min(block_set), max(block_set) + 1, size=(N, M)
        )
        return matrix

    def __repr__(self) -> str:
        text = (
            f'Grid:\n{self._matrix}\n\n' +
            '\n'.join([f"{k.value} = {k.name}"
                       for k in BlocksEnum])
        )
        text = f'{text}\n\nN = {self._height}\nM = {self._weight}'
        return text
