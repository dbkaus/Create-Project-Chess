class King:
    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.has_moved = False
        self.in_check = False
        
        self.x = 0
        self.y = 0