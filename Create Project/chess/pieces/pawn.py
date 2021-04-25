import

class Pawn:
    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.has_moved = False
        self.just_moved_two = False
        
        if self.color == white:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0