from Damas import DamasChinas
class Queen_Killer(DamasChinas):
    
    def Queen_Killer_W(self, Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final):
        #izquierda arriba a derecha abajo
        self.Row_Postion_Initial = Row_Postion_Initial
        self.Column_Postion_Initial = Column_Postion_Initial
        self.Row_Postion_Final = Row_Postion_Final
        self.Column_Postion_Final = Column_Postion_Final

        Value_Row_White = (Row_Postion_Initial - Row_Postion_Final)
        Value_Col_White = (Column_Postion_Initial - Column_Postion_Final)
        Value_row_int = int(Value_Row_White/2)
        Value_col_int = int(Value_Col_White/2)

        self.Board[Row_Postion_Final + Value_row_int][Column_Postion_Final + Value_col_int] = '◼'
        self.Board[Row_Postion_Final][Column_Postion_Final] = self.Pieses_Queen_Black
        self.Board[Row_Postion_Initial][Column_Postion_Initial] = '◼'
                    
