from moves import Move

class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.moves = list()
    
    def add_moves(self, move):
        self.moves.append(move)



