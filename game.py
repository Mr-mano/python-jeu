from random import randint
from player import Player

class Game:
    def __init__(self, number, nb_life, nb_essais, nb_aleatoire, name):
        self.number = number
        self.nb_life = nb_life
        self.nb_essais = nb_essais
        self.nb_aleatoire = nb_aleatoire
        self.player = Player(name, nb_life)


    def play(self):
        while self.nb_aleatoire != self.number and self.nb_essais < self.player.nb_life:
            print('essaie n° :', self.nb_essais)
            self.nb_aleatoire = int(input('entrez un nombre entre 0 et 10 : '))
            if self.nb_aleatoire > self.number:
                print('trop grand')
            elif self.nb_aleatoire < self.number:
                print('trop petit')
            else:
                print('tu as trouvé')
                self.nb_essais += 1

        if self.nb_essais == self.player.nb_life and self.nb_aleatoire != self.number:
            print('désolé, vous avez utilisé vos 5 essais')



if __name__ == "__main__":
    player_1 = Game(randint(0, 10),  5, 1, -1, 'Gérard')
    player_1.play()

    player_2 = Game(randint(0, 10),  5, 1, -1, 'Polo')
    player_2.play()






