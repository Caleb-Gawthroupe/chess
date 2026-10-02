"""
@author: Caleb Gawthroupe
"""

import board
class Piece:
    """
    A Piece superclass to represent a piece on the board
    Attributes:
        - location (tuple): the location of the piece on the board (column, row)
        - color (int): the color of the piece (0: white, 1: black)
        - legal_moves (list): a list of legal moves
        - value (int): the value of the piece
        - name (str): the name of the piece (p, r, n, b, q, k)
    """
    def __init__(self, location: tuple[int, int], color: int, value: int = 0, name: str="") -> None:
        self.location = location
        self.color = color
        self.legal_moves = []
        self.name = name

    def get_legal_moves(self) -> list:
        return self.legal_moves

    def valid_square(self, square: tuple[int, int], game_board: board.Board) -> bool:
        if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
            if game_board.is_empty(square):
                return True
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    return True
        return False

class Pawn(Piece):
    """
    A Pawn class to represent a pawn on the board
    Attributes:
    """
    def __init__(self, location: tuple[int, int], color: int) -> None:
        super().__init__(location, color, value=1, name="p")

    def has_moved(self) -> bool:
        """
        Returns whether the pawn has moved yet
        """
        if self.color == 0 and self.location[1] == 1:
            return False
        elif self.color == 1 and self.location[1] == 6:
            return False
        return True

    def check_diagonal(self, square: tuple[int, int], game_board: board.Board) -> bool:
        if not game_board.is_empty(square):
            piece = game_board.get_square(square)
            if piece.color != self.color:
                return True
        return False

    def update_legal_moves(self, game_board: board.Board) -> None:
        """
        Returns a list of legal moves in the form (column, row) i.e. (0, 1) = a2
        :return:
        """
        legal_moves = []
        color_flip = 1
        if self.color == 1: color_flip = -1 # Flip the direction we check if we are black

        # Check square in front of pawn
        square = (self.location[0], self.location[1] + 1*color_flip)
        if game_board.is_empty(square):
            legal_moves.append(square)

        # Check for two-move start
        square = (self.location[0], self.location[1] + 2*color_flip)
        if game_board.is_empty(square) and not self.has_moved():
            legal_moves.append(square)

        # Check for diagonals
        square1 = (self.location[0] + 1, self.location[1] + 1*color_flip)
        square2 = (self.location[0] -1, self.location[1] + 1*color_flip)
        if self.check_diagonal(square1, game_board): legal_moves.append(square1)
        if self.check_diagonal(square2, game_board): legal_moves.append(square2)

        self.legal_moves = legal_moves

class Rook(Piece):
    """
     A Rook class to represent a rook on the board
     Attributes:
     """

    def __init__(self, location: tuple[int, int], color: int) -> None:
        super().__init__(location, color, value=5, name="r")

    def check_upwards(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] <= 7:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0], square[1] + 1
        return legal_moves

    def check_downwards(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] >= 0:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0], square[1] - 1
        return legal_moves

    def check_left(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] >= 0:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1]
        return legal_moves

    def check_right(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1]
        return legal_moves

    def update_legal_moves(self, game_board: board.Board) -> None:
        """
        Updates the legal moves based on the current position
        :param board:
        :return:
        """
        legal_moves = []
        legal_moves.append(self.check_upwards(game_board)) # Check upwards
        legal_moves.append(self.check_downwards(game_board)) # Check downards
        legal_moves.append(self.check_left(game_board)) # Check left
        legal_moves.append(self.check_right(game_board)) # Check right

        self.legal_moves = legal_moves

class Bishop(Piece):
    """
     A Bishop class to represent a bishop on the board
     Attributes:
     """

    def __init__(self, location: tuple[int, int], color: int) -> None:
        super().__init__(location, color, value=3, name="b")

    def check_up_left(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] <= 7 and square[0] >= 0:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1] + 1
        return legal_moves

    def check_up_right(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7 and square[1] <= 7:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1] + 1
        return legal_moves

    def check_down_left(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] >= 0 and square[1] >= 0:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1] - 1
        return legal_moves

    def check_down_right(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7 and square[1] >= 0:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1] - 1
        return legal_moves

    def update_legal_moves(self, game_board: board.Board) -> None:
        """
        Updates the legal moves based on the current position
        :param board:
        :return:
        """
        legal_moves = []
        legal_moves.append(self.check_up_left(game_board)) # Check upwards
        legal_moves.append(self.check_up_right(game_board)) # Check downards
        legal_moves.append(self.check_down_left(game_board)) # Check left
        legal_moves.append(self.check_down_right(game_board)) # Check right

        self.legal_moves = legal_moves

class Queen(Piece):
    """
     A Queen class to represent a queen on the board
     Attributes:
     """

    def __init__(self, location: tuple[int, int], color: int) -> None:
        super().__init__(location, color, value=9, name="q")

    def check_up_left(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] <= 7 and square[0] >= 0:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1] + 1
        return legal_moves

    def check_up_right(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7 and square[1] <= 7:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1] + 1
        return legal_moves

    def check_down_left(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] >= 0 and square[1] >= 0:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1] - 1
        return legal_moves

    def check_down_right(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7 and square[1] >= 0:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1] - 1
        return legal_moves

    def check_upwards(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] <= 7:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0], square[1] + 1
        return legal_moves

    def check_downwards(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[1] >= 0:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0], square[1] - 1
        return legal_moves

    def check_left(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] >= 0:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] - 1, square[1]
        return legal_moves

    def check_right(self, game_board: board.Board) -> list[tuple[int, int]]:
        """
        :return: all upward legal moves
        """
        legal_moves = []
        # Check upwards
        square = self.location
        while square[0] <= 7:
            if game_board.is_empty(square):
                legal_moves.append(square)
            else:
                piece = game_board.get_square(square)
                if piece.color != self.color:
                    legal_moves.append(square)
                    return legal_moves
            square = square[0] + 1, square[1]
        return legal_moves

    def update_legal_moves(self, game_board: board.Board) -> None:
        """
        Updates the legal moves based on the current position
        :param board:
        :return:
        """
        legal_moves = []
        legal_moves.append(self.check_up_left(game_board))
        legal_moves.append(self.check_up_right(game_board))
        legal_moves.append(self.check_down_left(game_board))
        legal_moves.append(self.check_down_right(game_board))
        legal_moves.append(self.check_upwards(game_board))
        legal_moves.append(self.check_downwards(game_board))
        legal_moves.append(self.check_left(game_board))
        legal_moves.append(self.check_right(game_board))

        self.legal_moves = legal_moves

class Knight(Piece):
    """
     A Knight class to represent a Knight on the board
     Attributes:
     """

    def __init__(self, location: tuple[int, int], color: int) -> None:
        super().__init__(location, color, value=3, name="n")

    def check_horizontal(self, game_board: board.Board) -> list[tuple[int, int]]:
        legal_moves = []
        twos = [-2, 2]
        ones = [-1, 1]
        for h in twos:
            for v in ones:
                square = self.location[0] + h, self.location[1] + v
                if self.valid_square(square, game_board): legal_moves.append(square)

        return legal_moves

    def check_vertical(self, game_board: board.Board) -> list[tuple[int, int]]:
        legal_moves = []
        twos = [-2, 2]
        ones = [-1, 1]
        for h in ones:
            for v in twos:
                square = self.location[0] + h, self.location[1] + v
                if self.valid_square(square, game_board): legal_moves.append(square)

        return legal_moves

    def update_legal_moves(self, game_board: board.Board) -> None:
        """
        Updates the legal moves based on the current position
        :param board:
        :return:
        """
        legal_moves = []
        legal_moves.append(self.check_horizontal(game_board))
        legal_moves.append(self.check_vertical(game_board))

        self.legal_moves = legal_moves

class King(Piece):
    """
     A King class to represent a King on the board
     Attributes:
     """
    def __init__(self, location: tuple[int, int], color: int) -> None:
        super().__init__(location, color, value=0, name="k")

    def check_vertical(self, game_board: board.Board) -> list[tuple[int, int]]:
        legal_moves = []
        directions = [-1, 1]
        all_directions = [-1, 0, 1]
        for v in directions:
            for h in all_directions:
                square = self.location[0] + h, self.location[1] + v
                if self.valid_square(square, game_board): legal_moves.append(square)

        return legal_moves

    def check_sideways(self, game_board: board.Board) -> list[tuple[int, int]]:
        legal_moves = []
        directions = [-1, 1]
        for d in directions:
            square = self.location[0] + d, self.location[1]
            if self.valid_square(square, game_board): legal_moves.append(square)

        return legal_moves

    def update_legal_moves(self, game_board: board.Board) -> None:
        legal_moves = []
        legal_moves.append(self.check_vertical(game_board))
        legal_moves.append(self.check_sideways(game_board))

        self.legal_moves = legal_moves