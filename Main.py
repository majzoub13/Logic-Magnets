from Board import Board
from GameLogic import GameLogic
from Algorithms import Algorithms

board1 = Board(3, 4,[(2,0)],[],[(1,2)],[(1,1),(1,3)]) #1
board1.startBoard()
board2 = Board(5, 5,[(4,0)],[],[(1,2),(2,1),(2,3),(3,2)],[(0,2),(2,0),(2,2),(2,4),(4,2)]) #1
board2.startBoard()
board3 = Board(3, 4,[(2,0)],[],[(1,2)],[(0,3),(2,3)]) #2
board3.startBoard()
board4 = Board(5, 3,[(2,0)],[],[(1,1),(3,1)],[(0,0),(0,2),(4,1)])#2
board4.startBoard()
board5 = Board(4, 3,[(3,1)],[],[(1,0),(1,2),(2,0),(2,2)],[(0,0),(1,0),(3,0),(0,2),(1,2)])#2
board5.startBoard()
board6 = Board(3, 5,[(2,0)],[],[(1,1),(1,3)],[(1,2),(0,3),(2,3)])#2 unsolvable
board6.startBoard()
board7 = Board(5, 4,[(2,1)],[],[(1,0),(2,0),(3,1),(3,2)],[(0,0),(1,0),(2,3),(3,2),(4,3)])#2
board7.startBoard()
board8 = Board(3, 4,[(2,0)],[],[(1,1),(1,2)],[(0,0),(0,2),(2,2)])#2
board8.startBoard()
board9 = Board(1, 7,[(0,0)],[],[(0,3),(0,5)],[(0,1),(0,3),(0,6)])#2
board9.startBoard()
board10 = Board(4, 4,[(0,0)],[],[(2,2),(2,3),(3,1)],[(1,1),(1,3),(3,0),(3,3)])#2
board10.startBoard()
board11 = Board(2, 5,[],[(1,2)],[(0,0),(0,4)],[(0,1),(0,2),(0,3)])#1
board11.startBoard()
board12 = Board(5, 4,[],[(3,1)],[(0,0),(1,0),(4,3)],[(1,0),(2,0),(4,0),(4,2)])#1
board12.startBoard()
board13 = Board(3, 6,[],[(2,3)],[(0,0),(0,4),(0,5)],[(0,3),(2,1),(1,1),(0,4)])#2
board13.startBoard()
board14 = Board(4, 4,[],[(3,3)],[(0,3),(2,0),(3,0)],[(1,0),(1,2),(2,2),(2,1)])#2
board14.startBoard()
board15 = Board(3, 5,[(1,2)],[(2,2)],[(0,3),(0,1)],[(1,4),(0,0),(0,2),(2,4)])#2
board15.startBoard()
board16 = Board(5, 5,[(2,4)],[(2,0)],[(1,2),(3,2)],[(0,3),(0,4),(4,3),(4,0)])#3
board16.startBoard()
board17 = Board(4, 4,[(3,3)],[(0,0)],[(0,2),(2,0)],[(1,1),(1,3),(2,2),(3,1)])#2
board17.startBoard()
board18 = Board(5, 6,[(4,3)],[(4,2)],[(2,0),(0,3),(2,5)],[(2,3),(2,1),(2,2),(2,5),(1,3)])#2 unsolvable
board18.startBoard()
board19 = Board(5, 5,[(0,2)],[(2,2)],[(0,3),(0,1),(4,1),(4,3)],[(1,0),(3,0),(2,1),(3,2),(3,4),(1,4)])#4
board19.startBoard()
board20 = Board(5, 4,[(4,2)],[(4,3)],[(0,1),(0,2),(4,0)],[(0,1),(0,3),(1,0),(2,0),(3,0)])#2
board20.startBoard()
board21 = Board(3, 4,[(2,0)],[(2,3)],[(0,1),(1,1),(1,2)],[(1,0),(1,1),(0,2),(2,0),(2,1)])#2
board21.startBoard()
board22 = Board(4, 5,[(0,0)],[(3,2)],[(0,3),(0,4),(3,0)],[(0,1),(0,3),(1,0),(1,4),(2,1)])#3
board22.startBoard()
board23 = Board(4, 5,[(3,4)],[(3,2)],[(0,3),(1,4),(2,0)],[(0,2),(2,1),(2,2),(2,3),(3,2)])#3
board23.startBoard()
board24 = Board(5, 5,[(1,4)],[(3,0)],[(0,1),(1,3),(3,4)],[(0,3),(2,1),(2,3),(4,1),(4,2)])#3
board24.startBoard()
board25 = Board(5, 4,[(4,0)],[(0,3)],[(0,0),(1,2),(3,2),(4,3)],[(0,0),(0,3),(2,0),(4,0),(4,1),(4,2)])#3
board25.startBoard()

logic=GameLogic(2)
algorithms=Algorithms(logic)
algorithms.dfs(board5)
