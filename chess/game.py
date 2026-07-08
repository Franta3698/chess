import pieces
import board

gameBoard = board.setup_board()


wKing = pieces.King(1, 0, 3, 1)
wQueen = pieces.Queen(1, 0, 4, 2)
wBishops = list()
wKnights = list()
wRooks = list()
wPawns = list()
wBishops.append(pieces.Bishop(1, 0, 2, 3))
wBishops.append(pieces.Bishop(1, 0, 5, 4))
wKnights.append(pieces.Knight(1, 0, 1, 5))
wKnights.append(pieces.Knight(1, 0, 6, 6))
wRooks.append(pieces.Rook(1, 0, 0, 7))
wRooks.append(pieces.Rook(1, 0, 7, 8))

for i in range(8):
        wPawns.append(pieces.Pawn(1, 1, i, i + 9))


def board_loader(board, piecesList):
        pass

bPawns = list()

for i in range(8):
        bPawns.append(pieces.Pawn(-1, 6, i, i + 1))


board.print_board(gameBoard)