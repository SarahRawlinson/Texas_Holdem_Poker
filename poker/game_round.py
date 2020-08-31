class GameRound:
    def __init__(self, deck, players):
        self._deck = deck
        self._players = players
        self._community_cards = []
        self._community_pot = 0
        self.infinite = False
        self.game_qty = 1
        self.game_number = 0
        self.rounds = {1: {"bet": 0, "cards": 0}, 2: {"bet": 0, "cards": 3}, 3: {"bet": 0, "cards": 1},
                       4: {"bet": 0, "cards": 1}}

    def set_game_qty(self, infinite=False, game_qty=1):
        self.infinite = infinite
        self.game_qty = game_qty

    def print_new_game(self):
        print("*" * 50)
        print("#" * 50)
        print(f"New game!, Game {self.game_number}")
        print("*" * 20)
        names = []
        for player in self.check_for_active_players():
            names.append(player.name)
        names = ", ".join(names)
        print(f"Active Players : {names}")
        print("*" * 20)

    def play(self):

        while self.game_qty > 0 and len(self.check_for_active_players()) > 1:
            self.game_number += 1

            self.print_new_game()
            # shuffle cards
            self._shuffle_deck()
            # deal players
            self._deal_to_players()

            for round_number in self.rounds:
                # deal
                cards = self.rounds[round_number]["cards"]
                bet = self.rounds[round_number]["bet"]
                if cards > 0:
                    self._deal_community_cards(cards)
                self._new_round(round_number, bet)
                if len(self.check_for_active_players()) == 1:
                    break

            self.find_winner()
            community_cards = self._community_cards.copy()

            for player in self._players:
                cards = player.remove_cards()
                community_cards.extend(cards)
                if player.chips > 0:
                    player.active = True
                else:
                    player.active = False

            self._community_cards = []

            self._deck.add_cards(community_cards)

            if not self.infinite:
                self.game_qty -= 1

    def _new_round(self, number, bets):
        print("*" * 20)
        print(f"round {number} betting")
        print("*" * 20)
        print(f"Community cards : {self.community_cards}")
        print("*" * 10)
        # for player in self.check_for_active_players():
        #     print(f"{player.name} : cards : [{player.hand}] chips : [{player.chips}]")
        self.print_player_cards()
        print("*" * 10)
        self._check_for_bets(bets)
        print("*" * 10)
        print(f"Community pot : {self._community_pot}")

    def print_player_cards(self):
        for player in self.check_for_active_players():
            print(f"{player.name} : cards : [{player.two_cards}] chips : [{player.chips}] hand : [{player.hand.hand}] "
                  f"value : [{player.hand.score}]")

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
        first_round = True
        while bet_chips and len(self.check_for_active_players()) > 1:
            for player in self.check_for_active_players():
                if 1 == len(self.check_for_active_players()):
                    bet_chips = False
                    break
                player_bets.setdefault(player.name, 0)
                current_bets = player_bets[player.name]
                needed_bet = active_bet - current_bets
                if needed_bet > 0:
                    print(f"{player.name} needs to bet {needed_bet} to meet the active bet of {active_bet}")
                # if not first_round and needed_bet == 0 and player.active:
                #     break
                if needed_bet < 0:
                    needed_bet = 0
                bet = player.next_action(state, needed_bet, current_bets)
                # print(bet)
                player_bets[player.name] += int(bet)
                # bet = bet + needed_bet
                full_bet = bet + current_bets
                if full_bet > active_bet:
                    print(f"{player.name} raises {full_bet - active_bet}")
                    active_bet = bet + current_bets
                    state = "call"
                elif bet > 0:
                    print(f"{player.name} calls")
                    if not first_round:
                        self.bet(player, bet)
                        break
                elif player.active:
                    print(f"{player.name} checks")
                self.bet(player, bet)

            stop_run = False
            for active in self.check_for_active_players():
                # print(player_bets[active.name])
                # print(active.name)
                # print(active_bet)
                if player_bets[active.name] != active_bet:
                    stop_run = True
                    break


            bet_chips = stop_run
            first_round = False

    def bet(self, player, amount):
        if player.chips < amount:
            amount = player.chips
            print(f"{player.name} has gone all in")
        self._community_pot += player.bet(amount)
        print(f"{player.name} now has {player.chips} chips")

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
        for player in self.check_for_active_players():
            if player.hand.score > winning_score:
                winning_score = player.hand.score
                winner = [player]
                winners = [player]
            elif winning_score == player.hand.score:
                draw = True
                winners.append(player)
        self.print_winner(winners)

        if not draw:
            winner[0].add_chips(self._community_pot)
            name = winner[0].name
            chips = winner[0].chips
            print(f"{name} won {self._community_pot} chips")
            print(f"{name} now has {chips} chips")
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
                print(f"{names} all won {shared_pot} chips")
                self._community_pot = 0
            return winners

    def _get_community_cards(self):
        cards_as_strings = [str(card) for card in self._community_cards]
        return ", ".join(cards_as_strings)

    def _get_community_pot(self):
        return self._community_pot

    def print_winner(self, winner):
        if len(winner) == 1:
            winner = winner[0]
            print(f"The Winner is {winner.name} with a {winner.hand.hand}. "
                  f"The winning cards where {winner.hand.hand_cards}.")

        else:
            names = []
            for win in winner:
                names.append(win.name)
            names = " and ".join(names)
            print(f"Players Draw, winners are {names} the winning hands where {winner[0].hand}")

    deck = property(_get_deck)
    players = property(_get_players)
    community_cards = property(_get_community_cards)
    community_pot = property(_get_community_pot)
