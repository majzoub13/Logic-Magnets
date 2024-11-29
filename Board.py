from Pieces import Pieces


class Board:

    def __init__(self, n: int, m: int, p, r, g, w):
        self.n = n
        self.m = m
        self.p = p
        self.r = r
        self.g = g
        self.w = w
        self.playingBoard = [[Pieces(".") for _ in range(m)] for _ in range(n)]

    def startBoard(self):
        for w in self.w:
            self.playingBoard[w[0]][w[1]] = Pieces("W")
        for p in self.p:
            self.playingBoard[p[0]][p[1]] = Pieces("P")
        for r in self.r:
            self.playingBoard[r[0]][r[1]] = Pieces("R")
        for g in self.g:
            self.playingBoard[g[0]][g[1]] = Pieces("G")

    def __eq__(self, other):
        for i in range(self.n):
            for j in range(self.m):
                if self.playingBoard[i][j].char != other.playingBoard[i][j].char:
                    return False
        return True

    def __str__(self):
        output = "  "
        for j in range(self.m):
            output += f"{j} "  # column index
        output += "\n"
        for i in range(self.n):
            output += f"{i} "  # row index
            for j in range(self.m):
                piece = self.playingBoard[i][j]
                output += f"{piece} "  # print piece character
            output += "\n"
        return output

    def hillClimbHeuristic(self):
        boardCost = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.playingBoard[i][j].char == "G":
                    costs = []
                    for w in self.w:
                        x = abs((i - w[0]))
                        y = abs((j - w[1]))
                        cost = x + y
                        costs.append(cost)
                    boardCost = boardCost + min(costs)
                elif self.playingBoard[i][j].char in ["P", "R"]:
                    if (i, j) not in self.w:
                        boardCost = boardCost + 1
        return boardCost
