"""
@author: Caleb Gawthroupe
"""

import pygame
import pieces

class Board:
    """ Class used to represent a game board
    Attributes:
        board (list): A 2d list of the boards current state
    """
    def __init__(self):
        # 2d List containing board
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def is_empty(self, pos: tuple) -> bool:
        return self.board[pos[0]][pos[1]] == 0

    def get_square(self, pos: tuple[int, int]) -> pieces.Piece:
        """
        Method used to get a piece from the given square
        Pre Condition: not self.is_empty(pos)
        Pre Condition: 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7

        returns a Piece object
        """
        assert not self.is_empty(pos)
        return self.board[pos[0],pos[1]]