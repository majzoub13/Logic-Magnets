from copy import deepcopy


class Algorithms:

    def __init__(self, gameLogic):
        self.gameLogic = gameLogic
        self.states = []
        self.queue = []
        self.stack = []

    def bfs(self, startBoard):
        self.queue.append(deepcopy(startBoard))
        while len(self.queue) != 0:
            board = self.queue.pop(0)
            print(board)
            self.states.append(board)
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
                                    if temp not in self.states:
                                        self.queue.append(temp)

    def dfs(self, board):
        if self.gameLogic.checkWinForAlgorithms(board):
            print("You Win!")
            return
        self.states.append(deepcopy(board))
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
                                if temp not in self.states:
                                    self.stack.append(temp)
        nextBoard = self.stack.pop()
        print(nextBoard)
        self.dfs(nextBoard)

    def hillClimbing(self, board):
        minCost = board.heuristic()
        solvingBoard = board
        while True:
            neighbors = []
            for x in range(board.n):
                for y in range(board.m):
                    if board.playingBoard[x][y].char in ["P", "R"]:
                        for x2 in range(board.n):
                            for y2 in range(board.m):
                                newboard = deepcopy(board)
                                if self.gameLogic.isEmptySpace(newboard, x2, y2):
                                    self.gameLogic.movePiece(newboard, x, y, x2, y2)
                                    if newboard.playingBoard[x2][y2].char == "P":
                                        self.gameLogic.push(newboard, x2, y2)
                                    else:
                                        self.gameLogic.pull(newboard, x2, y2)
                                    newcost = newboard.heuristic()
                                    neighbors.append((newcost, newboard))
            minBoard = min(neighbors, key=lambda x: x[0])
            if minBoard[0] >= minCost:
                return minBoard[1]
            minCost = minBoard[0]
            solvingBoard = minBoard[1]
