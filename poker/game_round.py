class GameRound:
    def __init__(self, deck, players):
        self._deck = deck
        self._players = players
        self._community_cards = []
        self._community_pot = 0

    def play(self):

        # shuffle cards
        self._shuffle_deck()
        # deal players
        self._deal_to_players()
        # betting
        # deal flop
        self._deal_community_cards(3)
        # betting
        # deal turn
        self._deal_community_cards(1)
        # betting
        # deal river
        self._deal_community_cards(1)
        # winner found

        pass

    def _shuffle_deck(self):
        self._deck.shuffle()

    def _deal_to_players(self):
        for player in self.check_for_active_players():
            cards = self._deck.deal_cards(2)
            player.hand = cards

    def _deal_community_cards(self, amount):
        community_cards = self._deck.deal_cards(amount)
        self._community_cards.extend(community_cards)
        for player in self.check_for_active_players():
            player.hand = community_cards

    def bet(self, player, amount):
        self._community_pot += player.bet(amount)

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

    def _get_community_cards(self):
        return self._community_cards

    def _get_community_pot(self):
        return self._community_pot

    deck = property(_get_deck)
    players = property(_get_players)
    community_cards = property(_get_community_cards)
    community_pot = property(_get_community_pot)
