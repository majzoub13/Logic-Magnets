from copy import deepcopy


class Algorithms:

    def __init__(self, gameLogic):
        self.gameLogic = gameLogic
        self.visited = []
        self.queue = []
        self.stack = []

    def bfs(self, startBoard):
        self.queue.append(deepcopy(startBoard))
        while len(self.queue) != 0:
            board = self.queue.pop(0)
            print(board)
            self.visited.append(board)
            if self.gameLogic.checkWinForAlgorithms(board):
                print("You Win!")
                break
            for x in range(board.n):
                for y in range(board.m):
                    if board.playingBoard[x][y].char in ["P", "R"]:
                        for x2 in range(board.n):
                            for y2 in range(board.m):
                                temp = deepcopy(board)
                                if self.gameLogic.isEmptySpace(temp, x2, y2):
                                    self.gameLogic.movePiece(temp, x, y, x2, y2)
                                    if temp.playingBoard[x2][y2].char == "P":
                                        self.gameLogic.push(temp, x2, y2)
                                    else:
                                        self.gameLogic.pull(temp, x2, y2)
                                    if temp not in self.visited:
                                        self.queue.append(temp)

    def dfs(self, board):
        if self.gameLogic.checkWinForAlgorithms(board):
            print("You Win!")
            return
        self.visited.append(deepcopy(board))
        for x in range(board.n):
            for y in range(board.m):
                if board.playingBoard[x][y].char in ["P", "R"]:
                    for x2 in range(board.n):
                        for y2 in range(board.m):
                            temp = deepcopy(board)
                            if self.gameLogic.isEmptySpace(temp, x2, y2):
                                self.gameLogic.movePiece(temp, x, y, x2, y2)
                                if temp.playingBoard[x2][y2].char == "P":
                                    self.gameLogic.push(temp, x2, y2)
                                else:
                                    self.gameLogic.pull(temp, x2, y2)
                                if temp not in self.visited:
                                    self.stack.append(temp)
        nextBoard = self.stack.pop()
        print(nextBoard)
        self.dfs(nextBoard)
