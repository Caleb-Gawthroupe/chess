"""
@author: Caleb Gawthroupe
"""

import pygame
import pieces

class Board:
    """ Class used to represent a game board
    Attributes:
        board (list): A 2d list of the boards current state
        pieces (list): A list of all pieces on the board
    """
    def __init__(self):
        # 2d List containing board
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.piece_list = []
        self.generate_pieces()

    def __str__(self):
        lines = []
        for row in self.board:
            row_str = []
            for cell in row:
                if isinstance(cell, pieces.Piece):
                    row_str.append(f"{cell.name}{cell.color}")
                elif cell is None:
                    row_str.append(" . ")  # Placeholder for empty squares
                else:
                    row_str.append(str(cell))
            lines.append(" ".join(row_str))

        return "\n".join(lines)

    def generate_pieces(self) -> None:
        """
        Method used to generate a 2d list of the pieces
        :return:
        """
        # Add pawns
        for i in range(8):
            self.piece_list.append(pieces.Pawn(location=(1, i), color=1))
            self.piece_list.append(pieces.Pawn(location=(6, i), color=0))
        # Add rooks
        for col in [0, 7]:
            self.piece_list.append(pieces.Rook(location=(0, col), color=1))
            self.piece_list.append(pieces.Rook(location=(7, col), color=0))
        # Add Knights
        for col in [1, 6]:
            self.piece_list.append(pieces.Knight(location=(0, col), color=1))
            self.piece_list.append(pieces.Knight(location=(7, col), color=0))
        # Add Bishops
        for col in [2, 5]:
            self.piece_list.append(pieces.Bishop(location=(0, col), color=1))
            self.piece_list.append(pieces.Bishop(location=(7, col), color=0))
        # Add Kings
        self.piece_list.append(pieces.King(location=(0, 4), color=1))
        self.piece_list.append(pieces.King(location=(7, 4), color=0))
        # Add Queens
        self.piece_list.append(pieces.Queen(location=(0, 3), color=1))
        self.piece_list.append(pieces.Queen(location=(7, 3), color=0))

    def generate_board(self) -> None:
        """
        Method used to generate a 2d list of the boards
        :return:
        """
        for piece in self.piece_list:
            self.board[piece.location[0]][piece.location[1]] = piece

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


if __name__ == "__main__":
    board = Board()
    board.generate_board()
    print(board)