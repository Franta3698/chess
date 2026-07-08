import pieces
import board

gameBoard = board.setup_board()

bPawns = list()

for i in range(8):
        bPawns.append(pieces.Pawn(-1, 6, i, i + 1))


board.print_board(gameBoard)