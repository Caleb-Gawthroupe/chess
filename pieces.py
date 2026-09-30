"""
@author: Caleb Gawthroupe
"""

from board import Board

class Piece:
    """
    A Piece superclass to represent a piece on the board
    Attributes:
        - location (tuple): the location of the piece on the board (column, row)
        - color (int): the color of the piece (0: white, 1: black)
        - legal_moves (list): a list of legal moves
        - value (int): the value of the piece
    """
    def __init__(self, location: tuple[int, int], color: int, value: int = 0) -> None:
        self.location = location
        self.color = color
        self.legal_moves = []

    def get_legal_moves(self) -> list:
        return self.legal_moves

class Pawn(Piece):
    """
    A Pawn class to represent a pawn on the board
    Attributes:
    """
    def __init__(self, location: tuple[int, int], color: int) -> None:
        super().__init__(location, color, value=1)

    def has_moved(self) -> bool:
        """
        Returns whether the pawn has moved yet
        """
        if self.color == 0 and self.location[1] == 1:
            return False
        elif self.color == 1 and self.location[1] == 6:
            return False
        return True

    def check_diagonal(self, square: tuple[int, int], board: Board) -> bool:
        if not board.is_empty(square):
            piece = board.get_square(square)
            if piece.color != self.color:
                return True
        return False

    def update_legal_moves(self, board: Board) -> None:
        """
        Returns a list of legal moves in the form (column, row) i.e. (0, 1) = a2
        :return:
        """
        legal_moves = []
        color_flip = 1
        if self.color == 1: color_flip = -1 # Flip the direction we check if we are black

        # Check square in front of pawn
        square = (self.location[0], self.location[1] + 1*color_flip)
        if board.is_empty(square):
            legal_moves.append(square)

        # Check for two-move start
        square = (self.location[0], self.location[1] + 2*color_flip)
        if board.is_empty(square) and not self.has_moved():
            legal_moves.append(square)

        # Check for diagonals
        square1 = (self.location[0] + 1, self.location[1] + 1*color_flip)
        square2 = (self.location[0] -1, self.location[1] + 1*color_flip)
        if self.check_diagonal(square1, board): legal_moves.append(square1)
        if self.check_diagonal(square2, board): legal_moves.append(square2)

        self.legal_moves = legal_moves

class Rook(Piece):
    """
     A Rook class to represent a rook on the board
     Attributes:
     """

    def __init__(self, location: tuple[int, int], color: int) -> None:
        super().__init__(location, color, value=5)

    def check_upwards(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] <= 7:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0], square[1] + 1
        return legal_moves

    def check_downwards(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] >= 0:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0], square[1] - 1
        return legal_moves

    def check_left(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] >= 0:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1]
        return legal_moves

    def check_right(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1]
        return legal_moves

    def update_legal_moves(self, board: Board) -> None:
        """
        Updates the legal moves based on the current position
        :param board:
        :return:
        """
        legal_moves = []
        legal_moves.append(self.check_upwards(board)) # Check upwards
        legal_moves.append(self.check_downwards(board)) # Check downards
        legal_moves.append(self.check_left(board)) # Check left
        legal_moves.append(self.check_right(board)) # Check right

        self.legal_moves = legal_moves

class Bishop(Piece):
    """
     A Bishop class to represent a bishop on the board
     Attributes:
     """

    def __init__(self, location: tuple[int, int], color: int) -> None:
        super().__init__(location, color, value=3)

    def check_up_left(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] <= 7 and square[0] >= 0:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1] + 1
        return legal_moves

    def check_up_right(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7 and square[1] <= 7:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1] + 1
        return legal_moves

    def check_down_left(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] >= 0 and square[1] >= 0:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1] - 1
        return legal_moves

    def check_down_right(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7 and square[1] >= 0:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1] - 1
        return legal_moves

    def update_legal_moves(self, board: Board) -> None:
        """
        Updates the legal moves based on the current position
        :param board:
        :return:
        """
        legal_moves = []
        legal_moves.append(self.check_up_left(board)) # Check upwards
        legal_moves.append(self.check_up_right(board)) # Check downards
        legal_moves.append(self.check_down_left(board)) # Check left
        legal_moves.append(self.check_down_right(board)) # Check right

        self.legal_moves = legal_moves

class Queen(Piece):
    """
     A Queen class to represent a queen on the board
     Attributes:
     """

    def __init__(self, location: tuple[int, int], color: int) -> None:
        super().__init__(location, color, value=9)

    def check_up_left(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] <= 7 and square[0] >= 0:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1] + 1
        return legal_moves

    def check_up_right(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7 and square[1] <= 7:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1] + 1
        return legal_moves

    def check_down_left(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] >= 0 and square[1] >= 0:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1] - 1
        return legal_moves

    def check_down_right(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7 and square[1] >= 0:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1] - 1
        return legal_moves

    def check_upwards(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] <= 7:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0], square[1] + 1
        return legal_moves

    def check_downwards(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] >= 0:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0], square[1] - 1
        return legal_moves

    def check_left(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] >= 0:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1]
        return legal_moves

    def check_right(self, board: Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7:
            if board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1]
        return legal_moves

    def update_legal_moves(self, board: Board) -> None:
        """
        Updates the legal moves based on the current position
        :param board:
        :return:
        """
        legal_moves = []
        legal_moves.append(self.check_up_left(board))
        legal_moves.append(self.check_up_right(board))
        legal_moves.append(self.check_down_left(board))
        legal_moves.append(self.check_down_right(board))
        legal_moves.append(self.check_upwards(board))
        legal_moves.append(self.check_downwards(board))
        legal_moves.append(self.check_left(board))
        legal_moves.append(self.check_right(board))

        self.legal_moves = legal_moves

class Knight(Piece):
    """
     A Knight class to represent a Knight on the board
     Attributes:
     """

    def __init__(self, location: tuple[int, int], color: int) -> None:
        super().__init__(location, color, value=9)

    def check_horizontal(self, board: Board) -> list[tuple[int, int]]:
        legal_moves = []
        twos = [-2, 2]
        ones = [-1, 1]
        for h in twos:
            for v in ones:
                square = self.location[0] + h, self.location[1] + v
                if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
                    if board.is_empty(square):
                        legal_moves.append(square)
                    else:
                        piece = board.get_square(square)
                        if piece.color != self.color:
                            legal_moves.append(square)

        return legal_moves

    def check_vertical(self, board: Board) -> list[tuple[int, int]]:
        legal_moves = []
        twos = [-2, 2]
        ones = [-1, 1]
        for h in ones:
            for v in twos:
                square = self.location[0] + h, self.location[1] + v
                if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
                    if board.is_empty(square):
                        legal_moves.append(square)
                    else:
                        piece = board.get_square(square)
                        if piece.color != self.color:
                            legal_moves.append(square)

        return legal_moves

    def update_legal_moves(self, board: Board) -> None:
        """
        Updates the legal moves based on the current position
        :param board:
        :return:
        """
        legal_moves = []
        legal_moves.append(self.check_horizontal(board))
        legal_moves.append(self.check_vertical(board))

        self.legal_moves = legal_moves