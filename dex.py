from pokemon import Pokemon
from moves import Move
from trainer import Trainer

class Pokedex:
    def greet(self):
        print('Hello! Welcome to the Pokedex.')

    def create(self):
        trainer_name = input('What is your name? ')
        trainer_age = input('How old are you? ')
        trainer_city = input('What city are you from? ')
        trainer = Trainer(trainer_name, trainer_age, trainer_city)
        pokemon_name = input('What is the name of your pokemon? ')
        pokemon_type = input('What type is your pokemon? ')
        pokemon = Pokemon(pokemon_name, pokemon_type)
        pokemon_move = input('Enter its signature move: ')
        pokemon.add_moves(pokemon_move)
        print('Thank you for your information!')
        print('Here is your entry: ')
        trainer_list = ['Name: ' + trainer_name, 'Age: ' + trainer_age, 'City: ' + trainer_city]
        for i in trainer_list:
            print(i)
        pokemon_list = ['Pokemon: ' + pokemon_name, 'Type: ' + pokemon_type, 'Signature Move: ' + pokemon_move]
        for i in pokemon_list:
            print(i)

dex1 = Pokedex()
dex1.greet()
dex1.create()
