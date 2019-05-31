from swiss.player import Player

BYE = Player()


class Pairing:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


class Round:
    def __init__(self, players):
        self.pairings = []
        self.players = players

    def pair_round():
        pass
