from moves import Moves

class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.moves = list()
    
    def intro(self):
        print(f'{self.name} is a {self.type} type.')
        print(f"{self.name}'s moves are: ")
        for i in self.moves:
            print(i)
    
    def add_moves(self, move):
        self.moves.append(move)

pokemon = Pokemon('Pikachu', 'Electric')
pokemon.add_moves('thunderbolt')
pokemon.intro()



