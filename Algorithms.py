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
            self.states.append(board)
            if self.gameLogic.checkWinForAlgorithms(board):
                self.pathConstructor(board=board)
                print("You Win!")
                break
            for x in range(board.n):
                for y in range(board.m):
                    if board.playingBoard[x][y].char in ["P", "R"]:
                        for x2 in range(board.n):
                            for y2 in range(board.m):
                                temp = deepcopy(board)
                                temp.parent = board
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
            self.pathConstructor(board=board)
            print("You Win!")
            return
        self.states.append(deepcopy(board))
        for x in range(board.n):
            for y in range(board.m):
                if board.playingBoard[x][y].char in ["P", "R"]:
                    for x2 in range(board.n):
                        for y2 in range(board.m):
                            temp = deepcopy(board)
                            temp.parent = board
                            if self.gameLogic.isEmptySpace(temp, x2, y2):
                                self.gameLogic.movePiece(temp, x, y, x2, y2)
                                if temp.playingBoard[x2][y2].char == "P":
                                    self.gameLogic.push(temp, x2, y2)
                                else:
                                    self.gameLogic.pull(temp, x2, y2)
                                if temp not in self.states:
                                    self.stack.append(temp)
        nextBoard = self.stack.pop()
        self.dfs(nextBoard)

    def pathConstructor(self, board):
        path = []
        temp = board
        while temp != None:
            path.append(temp)
            temp = temp.parent
        path.reverse()
        for step in path:
            print(step)

    def ucs(self, board, cost):
        self.queue.append((cost, board))
        self.states.append(board)
        while len(self.queue) != 0:
            currentCost, currentBoard = self.queue.pop(0)
            if self.gameLogic.checkWinForAlgorithms(currentBoard):
                self.pathConstructor(board=currentBoard)
                print("You Win!")
                return
            for x in range(currentBoard.n):
                for y in range(currentBoard.m):
                    if board.playingBoard[x][y].char in ["P", "R"]:
                        for x2 in range(currentBoard.n):
                            for y2 in range(currentBoard.m):
                                if self.gameLogic.isEmptySpace(currentBoard, x2, y2):
                                    temp = deepcopy(currentBoard)
                                    temp.parent = currentBoard
                                    self.gameLogic.movePiece(temp, x, y, x2, y2)
                                    if temp.playingBoard[x2][y2].char == "P":
                                        self.gameLogic.push(temp, x2, y2)
                                    else:
                                        self.gameLogic.pull(temp, x2, y2)
                                    newCost = temp.ucsCost(currentCost)
                                    if temp not in self.states:
                                        self.queue.append((newCost, temp))
                                        self.queue.sort(key=lambda key: key[0])
        return

    def hillClimb(self, board):
        minCost = board.hillClimbHeuristic()
        solvingBoard = board
        while True:
            neighbors = []
            for x in range(solvingBoard.n):
                for y in range(solvingBoard.m):
                    if board.playingBoard[x][y].char in ["P", "R"]:
                        for x2 in range(solvingBoard.n):
                            for y2 in range(solvingBoard.m):
                                temp = deepcopy(board)
                                temp.parent = board
                                if self.gameLogic.isEmptySpace(temp, x2, y2):
                                    self.gameLogic.movePiece(temp, x, y, x2, y2)
                                    if temp.playingBoard[x2][y2].char == "P":
                                        self.gameLogic.push(temp, x2, y2)
                                    else:
                                        self.gameLogic.pull(temp, x2, y2)
                                    newcost = temp.hillClimbHeuristic()
                                    neighbors.append((newcost, temp))
            minBoard = min(neighbors, key=lambda key: key[0])
            if minBoard[0] >= minCost:
                self.pathConstructor(minBoard[1])
                return
            minCost = minBoard[0]
            solvingBoard = minBoard[1]
