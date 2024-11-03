from Pieces import Pieces
from Board import Board
from copy import deepcopy


class GameLogic:

    def __init__(self, board: Board, moves: int):
        self.board = board
        self.moves = moves
        self.win = False

    def play(self):
        print(f"Moves remaining: {self.moves}")
        print(self.board)
        while not self.win and self.moves > 0:
            try:
                print("Choose the piece you want to move:")
                x, y = self.getInputCoordinates()
                if not self.checkInput(x, y):
                    continue

                print("Where do you want to put the piece?")
                x2, y2 = self.getInputCoordinates()
                if not self.checkOutput(x2, y2):
                    continue

                self.movePiece(x, y, x2, y2)

                if self.board.playingBoard[x2][y2].char == "P":
                    self.push(x2, y2)
                elif self.board.playingBoard[x2][y2].char == "R":
                    self.pull(x2, y2)

                print(f"Moves remaining: {self.moves}")
                print(self.board)

                self.checkWin()

            except ValueError:
                print("Invalid input. Please enter integers.")

    def getInputCoordinates(self):
        x = int(input("Enter x="))
        y = int(input("Enter y="))
        return x, y

    def checkInRange(self, x, y):
        if x >= 0 and y >= 0 and x < self.board.n and y < self.board.m:
            return True
        else:
            return False

    def checkInput(self, x, y):
        if not self.checkInRange(x, y):
            print("Out of range")
            return False
        elif (
            self.board.playingBoard[x][y].char != "P"
            and self.board.playingBoard[x][y].char != "R"
        ):
            print("Wrong Piece")
            return False
        return True

    def checkOutput(self, x, y):
        if not self.checkInRange(x, y):
            print("Out of range")
            return False
        elif (
            self.board.playingBoard[x][y].char == "P"
            or self.board.playingBoard[x][y].char == "R"
            or self.board.playingBoard[x][y].char == "G"
        ):
            print("Can't place piece there")
            return False
        return True

    def checkWin(self):
        numberOfW = len(self.board.w)
        for w in self.board.w:
            piece = self.board.playingBoard[w[0]][w[1]]
            if piece.char != "W" and piece.char != ".":
                numberOfW -= 1
        if numberOfW == 0:
            self.win = True
            print("You win")

        elif self.moves == 0:
            print("You lose,No more moves")

    def isEmptySpace(self, x, y):  # returns true if spot is empty or can be moved into
        return self.checkInRange(x, y) and (
            self.board.playingBoard[x][y].char == "."
            or self.board.playingBoard[x][y].char == "W"
        )

    def isMovable(self, x, y):  # returns true if piece is moveable
        return (
            self.checkInRange(x, y)
            and self.board.playingBoard[x][y].char != "."
            and self.board.playingBoard[x][y].char != "W"
        )

    def isW(self, x, y):  # returns true if position is originally W
        return (x, y) in self.board.w

    def movePiece(self, x, y, x2, y2):
        self.moves -= 1
        self.board.playingBoard[x2][y2] = self.board.playingBoard[x][y]
        if self.isW(x, y):
            self.board.playingBoard[x][y] = Pieces("W")
        else:
            self.board.playingBoard[x][y] = Pieces(".")

    def push(self, x, y):
        for j in range(1, y, 1):  # push to the left
            if self.isMovable(x, j):
                if self.isEmptySpace(x, j - 1):
                    self.board.playingBoard[x][j - 1] = self.board.playingBoard[x][j]
                    if self.isW(x, j):
                        self.board.playingBoard[x][j] = Pieces("W")
                    else:
                        self.board.playingBoard[x][j] = Pieces(".")

        for j in range(self.board.m - 1, y, -1):  # push to the right
            if self.isMovable(x, j):
                if self.isEmptySpace(x, j + 1):
                    self.board.playingBoard[x][j + 1] = self.board.playingBoard[x][j]
                    if self.isW(x, j):
                        self.board.playingBoard[x][j] = Pieces("W")
                    else:
                        self.board.playingBoard[x][j] = Pieces(".")

        for i in range(1, x, 1):  # push up
            if self.isMovable(i, y):
                if self.isEmptySpace(i - 1, y):
                    self.board.playingBoard[i - 1][y] = self.board.playingBoard[i][y]
                    if self.isW(i, y):
                        self.board.playingBoard[i][y] = Pieces("W")
                    else:
                        self.board.playingBoard[i][y] = Pieces(".")

        for i in range(self.board.n - 1, x, -1):  # push down
            if self.isMovable(i, y):
                if self.isEmptySpace(i + 1, y):
                    self.board.playingBoard[i + 1][y] = self.board.playingBoard[i][y]
                    if self.isW(i, y):
                        self.board.playingBoard[i][y] = Pieces("W")
                    else:
                        self.board.playingBoard[i][y] = Pieces(".")

    def pull(self, x, y):
        for j in range(y - 1, -1, -1):  # pull from the left
            if self.isMovable(x, j):
                if self.isEmptySpace(x, j + 1):
                    self.board.playingBoard[x][j + 1] = self.board.playingBoard[x][j]
                    if self.isW(x, j):
                        self.board.playingBoard[x][j] = Pieces("W")
                    else:
                        self.board.playingBoard[x][j] = Pieces(".")

        for j in range(y + 1, self.board.m, 1):  # pull from the right
            if self.isMovable(x, j):
                if self.isEmptySpace(x, j - 1):
                    self.board.playingBoard[x][j - 1] = self.board.playingBoard[x][j]
                    if self.isW(x, j):
                        self.board.playingBoard[x][j] = Pieces("W")
                    else:
                        self.board.playingBoard[x][j] = Pieces(".")

        for i in range(x - 1, -1, -1):  # pull down
            if self.isMovable(i, y):
                if self.isEmptySpace(i + 1, y):
                    self.board.playingBoard[i + 1][y] = self.board.playingBoard[i][y]
                    if self.isW(i, y):
                        self.board.playingBoard[i][y] = Pieces("W")
                    else:
                        self.board.playingBoard[i][y] = Pieces(".")

        for i in range(x + 1, self.board.n, 1):  # pull up
            if self.isMovable(i, y):
                if self.isEmptySpace(i - 1, y):
                    self.board.playingBoard[i - 1][y] = self.board.playingBoard[i][y]
                    if self.isW(i, y):
                        self.board.playingBoard[i][y] = Pieces("W")
                    else:
                        self.board.playingBoard[i][y] = Pieces(".")
