class GameRound:
    def __init__(self, deck, players):
        self._deck = deck
        self._players = players

    def play(self):

        # shuffle cards
        self._shuffle_deck()
        # deal players
        self._deal_to_players()
        # betting
        # deal flop
        # betting
        # deal turn
        # betting
        # deal river
        # winner found
        pass

    def _shuffle_deck(self):
        self._deck.shuffle()

    def _deal_to_players(self):
        for player in self.check_for_active_players():
            cards = self._deck.deal_cards(2)
            player.hand = cards

    def _get_deck(self):
        return self._deck

    def _get_players(self):
        return self._players

    def check_for_active_players(self):
        player_list = []
        for player in self._players:
            if player.active:
                player_list.append(player)
        return player_list

    def check_for_inactive_players(self):
        player_list = []
        for player in self._players:
            if not player.active:
                player_list.append(player)
        return player_list

    deck = property(_get_deck)
    players = property(_get_players)
