class DamasChinas:
    def __init__(self):
        self.Pieses_White = "♟"
        self.Pieses_Black = "♙"
        self.Pieses_Queen_White = "♔"
        self.Pieses_Queen_Black = "♚"
        self.Board = []
        collumns = "x12345678"
        rows = "xABCDEFGH"
        for i in range(9):
            self.Board.append(['']*9)

        for i in range(0,9):
            for j in range(0,9):
                if((i+j)%2 == 0):
                    self.Board[i][j] = '◼'
                    if (i > 0 and i < 4):
                        
                        self.Board[i][j] = self.Pieses_White
                    if (i > 5):
                        self.Board[i][j] = self.Pieses_Black
                else:
                    self.Board[i][j] = '◻'

                self.Board[0][i] = collumns[i]
                self.Board[j][0] = rows[j]
        self.Board[6][4] = self.Pieses_White
        self.Board[8][6] = '◼'

    def state(self):
        for x in self.Board:
            print(x)


# LPiesesWB = DamasChinas()
# LPiesesWB.state()

# ⬛
# ⬜