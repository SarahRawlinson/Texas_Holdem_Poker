from time import sleep


def print_game_round(number):
    print("*" * 20)
    print(f"round {number} betting")
    print("*" * 20)


def print_community_cards(cards):
    cards_neat = neat_cards(cards)
    print(f"Community cards : {cards_neat}")
    print("*" * 10)


def neat_cards(cards):
    cards_as_strings = [str(card) for card in cards]
    cards_neat = ", ".join(cards_as_strings)
    return cards_neat


def print_player_cards(players):
    for player in players:
        print(f"{player.name} : cards : [{player.two_cards}] chips : [{player.chips}] hand : [{player.hand.hand}] "
              f"value : [{player.hand.score}]")
        print(f"Hand: {player.hand.hand_cards}")


def print_game_number(game_number):
    print("*" * 50)
    print("#" * 50)
    print(f"New game!, Game {game_number}")
    print("*" * 20)


def print_winner(winner, gui):
    if len(winner) == 1:
        winner = winner[0]
        GameRound.card_images(winner.hand.cards_in_hand, gui)
        gui.update_text_labels_winner(f"{winner.name} with {winner.hand.hand}")
        print(f"The Winner is {winner.name} with a {winner.hand.hand}. "
              f"The winning cards where {winner.hand.hand_cards}.")
    else:
        names = []
        hand = ""
        for win in winner:
            names.append(win.name)
            hand = win.hand.hand
            GameRound.card_images(win.hand.cards_in_hand, gui)
        names = " and ".join(names)
        gui.update_text_labels_winner(f"{names} with {hand}")
        print(f"Players Draw, winners are {names} the winning hands where {winner[0].hand.hand_cards}")


def print_community_pot(pot, gui):
    gui.update_text_labels_pot(pot)
    print("*" * 10)
    print(f"Community pot : {pot}")


def print_cards_back_in_deck(cards):
    print(f"cards back in deck. deck holds {len(cards)} cards.")


class GameRound:
    def __init__(self, deck, players, gui):
        self._gui = gui
        self._deck = deck
        self._players = players
        self._community_cards = []
        self._community_pot = 0
        self.infinite = False
        self.game_qty = 1
        self.game_number = 0
        self.must_bet = False
        self.rounds = {1: {"bet": 5, "cards": 0}, 2: {"bet": 0, "cards": 3}, 3: {"bet": 0, "cards": 1},
                       4: {"bet": 0, "cards": 1}}

    def set_game_qty(self, infinite=False, game_qty=1):
        self.infinite = infinite
        self.game_qty = game_qty

    def print_new_game(self):
        print_game_number(self.game_number)
        names = []
        for player in self.check_for_active_players():
            names.append(player.name)
        names = ", ".join(names)
        print(f"Active Players : {names}")
        print("*" * 20)

    def play(self):

        while self.game_qty > 0 and len(self.check_for_active_players()) > 1:
            self.show_new_cards()
            self.game_number += 1
            self.print_new_game()
            self._shuffle_deck()
            self._deal_to_players()
            self.play_rounds()
            self.find_winner()
            self.cards_back_to_deck()
            self._players.insert(0, self._players.pop(-1))
            if not self.infinite:
                self.game_qty -= 1

    def play_rounds(self):
        for round_number in self.rounds:
            cards = self.rounds[round_number]["cards"]
            bet = self.rounds[round_number]["bet"]
            if cards > 0:
                self._deal_community_cards(cards)
            self._new_round(round_number, bet)
            if len(self.check_for_active_players()) == 1:
                break

    def _new_round(self, number, bets):
        if bets > 0:
            self.must_bet = True
        print_game_round(number)
        print_community_cards(self._community_cards)
        players = [player for player in self.check_for_active_players() if player.controller.name == "Human"]
        print_player_cards(players)
        print("*" * 10)
        self._check_for_bets(bets)
        print_community_pot(self._community_pot, self._gui)

    def _shuffle_deck(self):
        self._deck.shuffle()

    def _deal_to_players(self):
        for player in self.check_for_active_players():
            cards = self._deck.deal_cards(2)
            player.hand = cards
            player.controller.update(2)

    def show_new_cards(self):
        cards = self._community_cards
        self.card_images(cards,self._gui)

    @staticmethod
    def card_images(cards, gui):
        number = int(len(cards))
        print(number)
        if number == 5:
            gui.change_card_image("C1", cards[0].file_name())
            gui.change_card_image("C2", cards[1].file_name())
            gui.change_card_image("C3", cards[2].file_name())
            gui.change_card_image("C4", cards[3].file_name())
            gui.change_card_image("C5", cards[4].file_name())
        elif number == 4:
            gui.change_card_image("C1", cards[0].file_name())
            gui.change_card_image("C2", cards[1].file_name())
            gui.change_card_image("C3", cards[2].file_name())
            gui.change_card_image("C4", cards[3].file_name())
            gui.change_card_image("C5", 'gray_back.png')
        elif number == 3:
            gui.change_card_image("C1", cards[0].file_name())
            gui.change_card_image("C2", cards[1].file_name())
            gui.change_card_image("C3", cards[2].file_name())
            gui.change_card_image("C4", 'gray_back.png')
            gui.change_card_image("C5", 'gray_back.png')
        elif number == 2:
            gui.change_card_image("C1", cards[0].file_name())
            gui.change_card_image("C2", cards[1].file_name())
            gui.change_card_image("C3", 'gray_back.png')
            gui.change_card_image("C4", 'gray_back.png')
            gui.change_card_image("C5", 'gray_back.png')
        elif number == 1:
            gui.change_card_image("C1", cards[0].file_name())
            gui.change_card_image("C2", 'gray_back.png')
            gui.change_card_image("C3", 'gray_back.png')
            gui.change_card_image("C4", 'gray_back.png')
            gui.change_card_image("C5", 'gray_back.png')
        else:
            gui.change_card_image("C1", 'gray_back.png')
            gui.change_card_image("C2", 'gray_back.png')
            gui.change_card_image("C3", 'gray_back.png')
            gui.change_card_image("C4", 'gray_back.png')
            gui.change_card_image("C5", 'gray_back.png')

    def _deal_community_cards(self, amount):
        community_cards = self._deck.deal_cards(amount)
        self._community_cards.extend(community_cards)
        self.show_new_cards()
        for player in self.check_for_active_players():
            player.hand = community_cards


    def _check_for_bets(self, start_bet):
        active_bet, bet_chips, first_round, last_player, player_all_in, player_bets = \
            self.check_if_need_to_bet(start_bet)
        self.while_betting_is_true(active_bet, bet_chips, first_round, last_player, player_all_in, player_bets,
                                   start_bet)

    def check_if_need_to_bet(self, start_bet):
        bet_chips = True
        active_bet = start_bet
        player_bets = {}
        first_round = True
        last_player = None
        player_all_in = False
        for player in self.check_for_active_players():
            if player.chips == 0:
                bet_chips = False
        return active_bet, bet_chips, first_round, last_player, player_all_in, player_bets

    def while_betting_is_true(self, active_bet, bet_chips, first_round,
                              last_player, player_all_in, player_bets, start_bet):
        if start_bet > 0:
            print("you need to bet")
            self.must_bet = True
        while bet_chips and len(self.check_for_active_players()) > 1:
            players = self.check_for_active_players()
            active_bet, player_all_in = self.betting_turns_each_player(active_bet, first_round, last_player,
                                                                       player_all_in, player_bets, players)
            stop_run = False
            if len(player_bets) > 1:
                stop_run = self.check_if_players_settled_bets(active_bet, player_all_in, player_bets, stop_run)
            bet_chips = stop_run
            first_round = False

    def betting_turns_each_player(self, active_bet, first_round, last_player, player_all_in, player_bets, players):
        for player in players:
            self._gui.show_text_labels_bet()
            self._gui.update_text_labels_bet(active_bet)
            if player == last_player:
                continue
            if self.must_bet:
                player.cant_fold = True
                self.must_bet = False
            last_player = player
            if 1 == len(self.check_for_active_players()):
                bet_chips = False
                break
            active_bet, bet, current_bets, full_bet, needed_bet, player_all_in = \
                self.check_players_bet(active_bet, player, player_all_in, player_bets)
            if full_bet > active_bet:
                active_bet = self.a_player_wants_to_raise(active_bet, bet, current_bets, full_bet, needed_bet, player)
            elif bet == needed_bet and needed_bet > 0:
                print(f"{player.name} calls")
                if not first_round:
                    self.bet(player, bet)
                    break
            elif not player.active:
                print(f"{player.name} folds")
            else:
                print(f"{player.name} checks")
            player.cant_fold = False
            self.check_if_player_leaves_game(bet, player)
            self._gui.hide_text_label_bet()
            sleep(.5)

        return active_bet, player_all_in

    def player_has_to_bet(self, bet, needed_bet, player):
        if self.must_bet and bet < needed_bet:
            print("You have to bet this round you cant fold")
            player.active = True
            player.cant_fold = False
            if player.chips > needed_bet:
                bet = needed_bet
            else:
                bet = player.chips
        return bet

    def check_if_player_leaves_game(self, bet, player):
        if player.active:
            self.bet(player, bet)
        else:
            print(f"{player.name} leaves the game")

    def check_players_bet(self, active_bet, player, player_all_in, player_bets):
        bet, current_bets, needed_bet = self.work_out_player_bet(active_bet, player, player_bets)
        active_bet, bet, player_all_in = self.player_goes_all_in(active_bet, bet, player, player_all_in,
                                                                 player_bets)
        bet, full_bet = self.set_player_bet(active_bet, bet, current_bets, player, player_all_in, player_bets)
        return active_bet, bet, current_bets, full_bet, needed_bet, player_all_in

    @staticmethod
    def set_player_bet(active_bet, bet, current_bets, player, player_all_in, player_bets):
        # if a player has gone in and current player wants to bet more
        if player_all_in and (bet + current_bets) > active_bet:
            bet = active_bet - current_bets
        player_bets[player.name] += int(bet)
        full_bet = bet + current_bets
        return bet, full_bet

    def work_out_player_bet(self, active_bet, player, player_bets):
        player_bets.setdefault(player.name, 0)
        current_bets = int(player_bets[player.name])
        needed_bet = self.work_out_needed_bet(active_bet, current_bets, player)
        bet = player.next_action(needed_bet, current_bets)
        bet = self.player_has_to_bet(bet, needed_bet, player)
        return bet, current_bets, needed_bet

    @staticmethod
    def work_out_needed_bet(active_bet, current_bets, player):
        needed_bet = int(active_bet) - int(current_bets)
        if needed_bet < 0:
            needed_bet = 0
        if needed_bet > 0 and player.active:
            print(f"{player.name} needs to bet {needed_bet} to meet the active bet of {active_bet}")
        return needed_bet

    @staticmethod
    def a_player_wants_to_raise(active_bet, bet, current_bets, full_bet, needed_bet, player):
        if needed_bet > 0:
            print(f"{player.name} raises {full_bet - active_bet}")
        else:
            print(f"{player.name} bets {full_bet}")
        active_bet = bet + current_bets
        return active_bet

    @staticmethod
    def player_goes_all_in(active_bet, bet, player, player_all_in, player_bets):
        if player.chips <= bet:
            player_all_in = True
            active_bet = player_bets[player.name] + player.chips
            print(f"{player.name} has gone all in!")
            bet = active_bet
        return active_bet, bet, player_all_in

    def check_if_players_settled_bets(self, active_bet, player_all_in, player_bets, stop_run):
        for active in self.check_for_active_players():
            if player_all_in and int(player_bets[active.name]) > int(active_bet):
                self._community_pot -= int(player_bets[active.name]) - active_bet
                active.add_chips(int(player_bets[active.name]) - active_bet)
            elif int(player_bets[active.name]) != int(active_bet):
                stop_run = True
                break
        return stop_run

    def bet(self, player, amount):
        self._community_pot += player.bet(amount)
        print(f"{player.name} now has {player.chips} chips")
        print_community_pot(self._community_pot, self._gui)

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
        print_community_cards(self._community_cards)
        print_winner(winners, self._gui)
        if not draw:
            return self.winners_draw(winner)
        else:
            return self.single_winner(winners)

    def winners_draw(self, winner):
        winner[0].add_chips(self._community_pot)
        name = winner[0].name
        chips = winner[0].chips
        print(f"{name} won {self._community_pot} chips")
        print(f"{name} now has {chips} chips")
        self._community_pot = 0
        return winner

    def single_winner(self, winners):
        if self._community_pot > 0:
            shared_pot = int(self._community_pot / len(winners))
            names = []
            for winner_name in winners:
                winner_name.add_chips(shared_pot)
                names.append(winner_name.name)
            names = ", ".join(names)
            print(f"{names} all won {shared_pot} chips")
            self._community_pot -= (shared_pot * len(winners))
        return winners

    def _get_community_cards(self):
        cards_as_strings = [str(card) for card in self._community_cards]
        return ", ".join(cards_as_strings)

    def _get_community_pot(self):
        return self._community_pot

    def cards_back_to_deck(self):
        community_cards = self._community_cards.copy()
        self.reset_game(community_cards)
        self._community_cards = []
        self._deck.add_cards(community_cards)
        print_cards_back_in_deck(self.deck.cards)

    def reset_game(self, community_cards):
        for player in self._players:
            cards = player.remove_cards()
            community_cards.extend(cards)
            if player.chips > 0:
                player.active = True
            else:
                player.active = False

    deck = property(_get_deck)
    players = property(_get_players)
    community_cards = property(_get_community_cards)
    community_pot = property(_get_community_pot)
