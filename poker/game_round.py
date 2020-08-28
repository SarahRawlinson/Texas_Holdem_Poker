class Game_Round():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def play(self):

        # shuffle cards
        self.deck.shuffle()
        # deal players
        for player in self.players:
            self.deck.deal_cards(2)
        # betting
        # deal flop
        # betting
        # deal turn
        # betting
        # deal river
        # winner found
        pass
