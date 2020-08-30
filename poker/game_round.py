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
        print("*" * 10)
        print("round 1 betting")
        print("*" * 10)
        self._check_for_bets(5)
        # deal flop
        self._deal_community_cards(3)
        # betting
        print("*" * 10)
        print("round 2 betting")
        print("*" * 10)
        self._check_for_bets(0)
        # deal turn
        self._deal_community_cards(1)
        # betting
        print("*" * 10)
        print("round 3 betting")
        print("*" * 10)
        self._check_for_bets(0)
        # deal river
        self._deal_community_cards(1)
        # final bet
        print("*" * 10)
        print("round 4 betting")
        print("*" * 10)
        self._check_for_bets(0)
        # winner found
        # winner = self._find_winner()

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

    def _check_for_bets(self, start_bet):
        bet_chips = True
        active_bet = start_bet
        if start_bet > 0:
            state = "call"
        else:
            state = "check"
        player_bets = {}
        while bet_chips and len(self.check_for_active_players()) > 1:
            for player in self.check_for_active_players():
                player_bets.setdefault(player.name, 0)
                current_bets = player_bets[player.name]
                needed_bet = active_bet - current_bets
                bet = player.next_action(state, needed_bet)
                player_bets[player.name] += int(bet)
                # bet = bet + needed_bet
                full_bet = bet
                if full_bet > active_bet:
                    print(f"{player.name} raises {full_bet - active_bet}")
                    active_bet = bet + needed_bet
                    state = "call"
                elif bet > 0:
                    print(f"{player.name} bet {bet}")
                self.bet(player, bet)

            match = False
            for player in self.check_for_active_players():
                if player_bets[player.name] != active_bet:
                    match = True
            bet_chips = match

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

    def find_winner(self):
        winner = None
        winners = []
        winning_score = 0
        draw = False
        for player in self._players:
            if player.hand.value > winning_score:
                winning_score = player.hand.value
                winner = [player]
                winners = [player]
            elif winning_score == player.hand.value:
                draw = True
                winners.append(player)

        if not draw:
            winner[0].add_chips(self._community_pot)
            name = winner[0].name
            print(f"The winner is {name} winning {self._community_pot} chips")
            self._community_pot = 0
            return winner
        else:
            if self._community_pot > 0:
                shared_pot = self._community_pot / len(winners)
                names = []
                for winner_name in winners:
                    winner_name.add_chips(shared_pot)
                    names.append(winner_name.name)
                names = ", ".join(names)
                print(f"The winners are {names} winning {shared_pot} chips")
                self._community_pot = 0
            return winners

    def _get_community_cards(self):
        return self._community_cards

    def _get_community_pot(self):
        return self._community_pot

    deck = property(_get_deck)
    players = property(_get_players)
    community_cards = property(_get_community_cards)
    community_pot = property(_get_community_pot)
