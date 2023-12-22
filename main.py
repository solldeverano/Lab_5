class Piece:
    def __init__(self, position, color, number_of_moves, move_rule):
        self.position = position
        self.color = color
        self.number_of_moves = number_of_moves
        self.move_rule = move_rule

    def move(self, new_position):
        if self.check_position_range(new_position):
            self.position = new_position
            self.number_of_moves += 1
            moves = self.move_rule.get_all_moves()
            return {"valid": True, "moves": moves}
        else:
            return {"valid": False, "error": "Invalid position"}

    @staticmethod
    def check_position_range(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    def __str__(self):
        return f"Piece at {self.position}, Color: {self.color}, Moves: {self.number_of_moves}"

    def print_info(self):
        print(str(self))


class KnightMove:
    def __init__(self, position):
        self.position = position

    def get_all_moves(self):
        x, y = self.position
        possible_moves = [
            (x + 2, y + 1), (x + 1, y + 2),
            (x + 2, y - 1), (x + 1, y - 2),
            (x - 2, y + 1), (x - 1, y + 2),
            (x - 2, y - 1), (x - 1, y - 2)
        ]
        return [(new_x, new_y) for new_x, new_y in possible_moves if Piece.check_position_range((new_x, new_y))]


class BishopMove:
    def __init__(self, position):
        self.position = position

    def get_all_moves(self):
        x, y = self.position
        moves = []
        for i in range(1, 8):
            self.add_move_if_valid(x + i, y + i, moves)
            self.add_move_if_valid(x - i, y + i, moves)
            self.add_move_if_valid(x + i, y - i, moves)
            self.add_move_if_valid(x - i, y - i, moves)
        return moves

    def add_move_if_valid(self, x, y, moves):
        if Piece.check_position_range((x, y)):
            moves.append((x, y))


class KingMove:
    def __init__(self, position):
        self.position = position

    def get_all_moves(self):
        x, y = self.position
        possible_moves = [
            (x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1),
            (x + 1, y + 1), (x - 1, y + 1),
            (x + 1, y - 1), (x - 1, y - 1)
        ]
        return [(new_x, new_y) for new_x, new_y in possible_moves if Piece.check_position_range((new_x, new_y))]


class RookMove:
    def __init__(self, position):
        self.position = position

    def get_all_moves(self):
        x, y = self.position
        moves = []
        for i in range(1, 8):
            self.add_move_if_valid(x + i, y, moves)
            self.add_move_if_valid(x - i, y, moves)
            self.add_move_if_valid(x, y + i, moves)
            self.add_move_if_valid(x, y - i, moves)
        return moves

    def add_move_if_valid(self, x, y, moves):
        if Piece.check_position_range((x, y)):
            moves.append((x, y))


class Knight(Piece):
    def __init__(self, position, color):
        super().__init__(position, color, 0, KnightMove(position))

    def print_info(self):
        print(str(self))


class Bishop(Piece):
    def __init__(self, position, color):
        super().__init__(position, color, 0, BishopMove(position))

    def print_info(self):
        print(str(self))


class King(Piece):
    def __init__(self, position, color):
        super().__init__(position, color, 0, KingMove(position))

    def print_info(self):
        print(str(self))


class Rook(Piece):
    def __init__(self, position, color):
        super().__init__(position, color, 0, RookMove(position))

    def print_info(self):
        print(str(self))


def main():
    bishop = Bishop((3, 3), color="Black")

    print(bishop.move((6, 6)))

    print(bishop.move((8, 8)))

    print(bishop.move((5, 1)))

    bishop.print_info()

    king = King((4, 4), color="White")

    print(king.move((5, 5)))

    print(king.move((8, 8)))

    print(king.move((3, 4)))

    king.print_info()


if __name__ == "__main__":
    main()
