from Pieces import Pieces
from Board import Board
from copy import deepcopy


class GameLogic:

    def __init__(self, moves: int):
        self.moves = moves
        self.win = False

    def play(self, board):
        print(f"Moves remaining: {self.moves}")
        print(board)
        while not self.win and self.moves > 0:
            try:
                print("Choose the piece you want to move:")
                x, y = self.getInputCoordinates()
                if not self.checkInput(board, x, y):
                    continue

                print("Where do you want to put the piece?")
                x2, y2 = self.getInputCoordinates()
                if not self.checkOutput(board, x2, y2):
                    continue

                self.movePiece(board, x, y, x2, y2)

                if board.playingBoard[x2][y2].char == "P":
                    self.push(board, x2, y2)
                elif board.playingBoard[x2][y2].char == "R":
                    self.pull(board, x2, y2)

                print(f"Moves remaining: {self.moves}")
                print(board)

                self.checkWin(board)

            except ValueError:
                print("Invalid input. Please enter integers.")

    def getInputCoordinates(self):
        x = int(input("Enter x="))
        y = int(input("Enter y="))
        return x, y

    def checkInRange(self, board, x, y):
        if x >= 0 and y >= 0 and x < board.n and y < board.m:
            return True
        else:
            return False

    def checkInput(self, board, x, y):
        if not self.checkInRange(board, x, y):
            print("Out of range")
            return False
        elif (
            board.playingBoard[x][y].char != "P"
            and board.playingBoard[x][y].char != "R"
        ):
            print("Wrong Piece")
            return False
        return True

    def checkOutput(self, board, x, y):
        if not self.checkInRange(board, x, y):
            print("Out of range")
            return False
        elif (
            board.playingBoard[x][y].char == "P"
            or board.playingBoard[x][y].char == "R"
            or board.playingBoard[x][y].char == "G"
        ):
            print("Can't place piece there")
            return False
        return True

    def checkWin(self, board):
        numberOfW = len(board.w)
        for w in board.w:
            piece = board.playingBoard[w[0]][w[1]]
            if piece.char != "W" and piece.char != ".":
                numberOfW -= 1
        if numberOfW == 0:
            self.win = True
            print("You win")

        elif self.moves == 0:
            print("You lose,No more moves")

    def checkWinForAlgorithms(self, board):
        numberOfW = len(board.w)
        for w in board.w:
            piece = board.playingBoard[w[0]][w[1]]
            if piece.char != "W" and piece.char != ".":
                numberOfW -= 1
        if numberOfW == 0:
            return True
        else:
            return False

    def isEmptySpace(
        self, board, x, y
    ):  # returns true if spot is empty or can be moved into
        return self.checkInRange(board, x, y) and (
            board.playingBoard[x][y].char == "." or board.playingBoard[x][y].char == "W"
        )

    def isMovable(self, board, x, y):  # returns true if piece is moveable
        return (
            self.checkInRange(board, x, y)
            and board.playingBoard[x][y].char != "."
            and board.playingBoard[x][y].char != "W"
        )

    def isW(self, board, x, y):  # returns true if position is originally W
        return (x, y) in board.w

    def movePiece(self, board, x, y, x2, y2):
        self.moves -= 1
        board.playingBoard[x2][y2] = board.playingBoard[x][y]
        if self.isW(board, x, y):
            board.playingBoard[x][y] = Pieces("W")
        else:
            board.playingBoard[x][y] = Pieces(".")

    def push(self, board, x, y):
        for j in range(1, y, 1):  # push to the left
            if self.isMovable(board, x, j):
                if self.isEmptySpace(board, x, j - 1):
                    board.playingBoard[x][j - 1] = board.playingBoard[x][j]
                    if self.isW(board, x, j):
                        board.playingBoard[x][j] = Pieces("W")
                    else:
                        board.playingBoard[x][j] = Pieces(".")

        for j in range(board.m - 1, y, -1):  # push to the right
            if self.isMovable(board, x, j):
                if self.isEmptySpace(board, x, j + 1):
                    board.playingBoard[x][j + 1] = board.playingBoard[x][j]
                    if self.isW(board, x, j):
                        board.playingBoard[x][j] = Pieces("W")
                    else:
                        board.playingBoard[x][j] = Pieces(".")

        for i in range(1, x, 1):  # push up
            if self.isMovable(board, i, y):
                if self.isEmptySpace(board, i - 1, y):
                    board.playingBoard[i - 1][y] = board.playingBoard[i][y]
                    if self.isW(board, i, y):
                        board.playingBoard[i][y] = Pieces("W")
                    else:
                        board.playingBoard[i][y] = Pieces(".")

        for i in range(board.n - 1, x, -1):  # push down
            if self.isMovable(board, i, y):
                if self.isEmptySpace(board, i + 1, y):
                    board.playingBoard[i + 1][y] = board.playingBoard[i][y]
                    if self.isW(board, i, y):
                        board.playingBoard[i][y] = Pieces("W")
                    else:
                        board.playingBoard[i][y] = Pieces(".")

    def pull(self, board, x, y):
        for j in range(y - 1, -1, -1):  # pull from the left
            if self.isMovable(board, x, j):
                if self.isEmptySpace(board, x, j + 1):
                    board.playingBoard[x][j + 1] = board.playingBoard[x][j]
                    if self.isW(board, x, j):
                        board.playingBoard[x][j] = Pieces("W")
                    else:
                        board.playingBoard[x][j] = Pieces(".")

        for j in range(y + 1, board.m, 1):  # pull from the right
            if self.isMovable(board, x, j):
                if self.isEmptySpace(board, x, j - 1):
                    board.playingBoard[x][j - 1] = board.playingBoard[x][j]
                    if self.isW(board, x, j):
                        board.playingBoard[x][j] = Pieces("W")
                    else:
                        board.playingBoard[x][j] = Pieces(".")

        for i in range(x - 1, -1, -1):  # pull down
            if self.isMovable(board, i, y):
                if self.isEmptySpace(board, i + 1, y):
                    board.playingBoard[i + 1][y] = board.playingBoard[i][y]
                    if self.isW(board, i, y):
                        board.playingBoard[i][y] = Pieces("W")
                    else:
                        board.playingBoard[i][y] = Pieces(".")

        for i in range(x + 1, board.n, 1):  # pull up
            if self.isMovable(board, i, y):
                if self.isEmptySpace(board, i - 1, y):
                    board.playingBoard[i - 1][y] = board.playingBoard[i][y]
                    if self.isW(board, i, y):
                        board.playingBoard[i][y] = Pieces("W")
                    else:
                        board.playingBoard[i][y] = Pieces(".")
