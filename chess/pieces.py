class Piece:
    def __init__(self, colorNum, row, col, id, taken = False):
        self.row = row
        self.col = col
        self.id = id
        self.colorNum = colorNum
        self.taken = taken
    def print_color(self):
        if self.colorNum > 0:
            print("white")
        else:
            print("black")
    
class King(Piece):
    def valid_moves_check(self, board):
        pass
    def print_type(self):
        print("King")

class Queen(Piece):
    def valid_moves_check(self, board):
        pass
    def print_type(self):
        print("Queen")

class Bishop(Piece):
    def valid_moves_check(self, board):
        pass
    def print_type(self):
        print("Bishop")

class Knight(Piece):
    def valid_moves_check(self, board):
        pass
    def print_type(self):
        print("Knight")

class Rook(Piece):
    def valid_moves_check(self, board):
        pass
    def print_type(self):
        print("Rook")        

class Pawn(Piece):
    def valid_moves_check(self, board):
        pass
    def print_type(self):
        print("Pawn")

if __name__ == "__main__":
    bPawns = list()

    for i in range(8):
        bPawns.append(Pawn(-1, 6, i, i))

