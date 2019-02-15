class Player:
    def __init__(self, name, nb_life):
        self.name = name
        self.nb_life = nb_life

if __name__ == "__main__":
    player_1 = Player('gérard', 5)
    print('prénom : ', player_1.name, 'Point de vie : ', player_1.nb_life)



