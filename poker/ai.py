import random
from time import sleep



class AI:
    def __init__(self, player):
        self.name = "AI"
        self.fold = False
        self.player = player
        self.wants_to_bet = False
        self.check = True
        self.call = True
        self.bet_qty = 0
        self.all_in = False
        self.raise_bet = False
        self.min_bet = 0
        player.controller = self

    def update(self, number):
        return

    def make_decision(self, bet, total_bet):
        self.min_bet = bet
        wants_to_bluff = False
        if bet > 0:
            # self.check_for_call(bet)
            if self.raise_bet:
                self.wants_to_bet = True
                self.bet()
                wants_to_bluff = random.choice([True, False, False, False])
        else:
            wants_to_bluff = self._no_existing_bets(total_bet, wants_to_bluff)
        if wants_to_bluff:
            # print(f"{self.player.name} decides to change change there mind")
            self.bluff()
        # self.bet_qty = bet + self.bet_qty

    def _no_existing_bets(self, total_bet, wants_to_bluff):
        if self.player.chips > 50 and (total_bet < self.player.chips / 10) and self.player.hand.score >= 110:
            wants_to_bluff = self.decides_to_bet(wants_to_bluff)
        else:
            # print(f"{self.player.name} decides not to bet")
            self.wants_to_bet = False
            self.check = True
        return wants_to_bluff

    def decides_to_bet(self, wants_to_bluff):
        # print(f"{self.player.name} thinks they should bet")
        self.wants_to_bet = True
        self.bet()
        self.check = False
        wants_to_bluff = random.choice([True, False, False, False])
        return wants_to_bluff

    def print_chips(self):
        return

    def bet(self):
        card_amount = len(self.player.hand.cards)
        card_value = self.player.hand.score
        amount_to_bet = self._check_cards_for_bet(card_amount, card_value)
        # print(f"{self.player.name} thinks they should bet {amount_to_bet}")
        if amount_to_bet > self.player.chips:
            amount_to_bet = self.player.chips
        self.bet_qty = amount_to_bet

    def _check_cards_for_bet(self, card_amount, card_value):
        if card_amount == 2:
            amount_to_bet = self._two_card_bet(card_value)
        elif card_amount == 5:
            amount_to_bet = self._five_card_bet(card_value)
        elif card_amount == 6:
            amount_to_bet = self._six_card_bet(card_value)
        elif card_amount == 7:
            amount_to_bet = self._seven_card_bet(card_value)
        else:
            amount_to_bet = 2
        if self.player.cant_fold and amount_to_bet == 0:
            amount_to_bet = self.min_bet
        return amount_to_bet

    def _seven_card_bet(self, card_value):
        if card_value > 300:
            amount_to_bet = 20
        elif card_value > 400:
            amount_to_bet = 30
        else:
            amount_to_bet = 2
        return amount_to_bet

    def _six_card_bet(self, card_value):
        if card_value > 250:
            amount_to_bet = 10
        elif card_value > 300:
            amount_to_bet = 30
        else:
            amount_to_bet = 2
        return amount_to_bet

    def _five_card_bet(self, card_value):
        if card_value > 200:
            amount_to_bet = 10
        elif card_value > 300:
            amount_to_bet = 30
        else:
            amount_to_bet = 5
        return amount_to_bet

    def _two_card_bet(self, card_value):
        if card_value > 110:
            amount_to_bet = 10
        elif card_value > 200:
            amount_to_bet = 30
        else:
            amount_to_bet = 5
        return amount_to_bet

    def bluff(self):
        random_choice = random.choice([0, 1, 2, 3, 4, 5])
        if self.player.chips > 30:
            self._try_function(random_choice)

    def _try_function(self, args):
        get_function = {0: self._drop_bet,
                        1: self._no_change,
                        2: self._change_top_bet,
                        3: self._change_high_bet,
                        4: self._change_med_bet,
                        5: self._change_low_bet}
        func = get_function.get(int(args), "nothing")
        return func()

    def _drop_bet(self):
        print(f"{self.player.name} decides not to bet")
        self.bet_qty = 0
        self.wants_to_bet = False

    def _no_change(self):
        print(f"{self.player.name} decides to stick with there first thought")
        pass

    def _change_top_bet(self):
        print(f"{self.player.name} decides to change to bet to 30")
        self.bet_qty = 30
        self.wants_to_bet = True

    def _change_high_bet(self):
        print(f"{self.player.name} decides to change to bet to 20")
        self.bet_qty = 20
        self.wants_to_bet = True

    def _change_low_bet(self):
        print(f"{self.player.name} decides to change to bet to 2")
        self.bet_qty = 2
        self.wants_to_bet = True

    def _change_med_bet(self):
        print(f"{self.player.name} decides to change to bet to 5")
        self.bet_qty = 5
        self.wants_to_bet = True

    def check_for_call(self, amount, total_bet):
        if self.player.chips == 0:
            return
        card_amount = len(self.player.hand.cards)
        card_value = self.player.hand.score
        call = False
        raise_bet = False
        all_in = False
        fold = False
        all_in, call, fold, raise_bet = self._check_cards_for_call(all_in, amount, call, card_amount, card_value, fold,
                                                                   raise_bet)
        self.call = call
        self.all_in = all_in
        self.raise_bet = raise_bet
        self.fold = fold
        self._print_call_thought(all_in, call, fold, raise_bet)

    def _check_cards_for_call(self, all_in, amount, call, card_amount, card_value, fold, raise_bet):
        if amount > 5:
            if self.player.chips > amount:
                call, fold, raise_bet = self._enough_chips_call(call, card_amount, card_value, fold, raise_bet)
            else:
                all_in, fold = self._bet_to_call_higher_than_player_chips(all_in, card_value, fold)
        else:
            call, fold, raise_bet = self._call_on_low_value_bet(call, card_value, fold, raise_bet)
        if self.player.chips < 50 and raise_bet:
            raise_bet = False
            call = True
        return all_in, call, fold, raise_bet

    def _bet_to_call_higher_than_player_chips(self, all_in, card_value, fold):
        if card_value >= 400:
            all_in = True
        else:
            fold = True
        return all_in, fold

    def _call_on_low_value_bet(self, call, card_value, fold, raise_bet):
        if card_value > 300:
            raise_bet = True
        elif card_value > 110:
            call = True
        elif self.player.cant_fold:
            call = True
        else:
            fold = True
        return call, fold, raise_bet

    def _enough_chips_call(self, call, card_amount, card_value, fold, raise_bet):
        if card_value >= 300:
            raise_bet = True
        elif card_amount == 2:
            call, fold, raise_bet = self._two_cards_call(call, card_value, fold, raise_bet)
        elif card_amount == 5:
            call, fold, raise_bet = self._five_cards_call(call, card_value, fold, raise_bet)
        elif card_amount == 6:
            call, fold, raise_bet = self._six_card_call(call, card_value, fold, raise_bet)
        elif card_amount == 7:
            call, fold = self._seven_card_call(call, card_value, fold)
        if self.player.cant_fold and fold:
            fold = False
        return call, fold, raise_bet

    def _seven_card_call(self, call, card_value, fold):
        if card_value >= 200:
            call = True
        else:
            fold = True
        return call, fold

    def _six_card_call(self, call, card_value, fold, raise_bet):
        if card_value > 300:
            raise_bet = True
        elif card_value >= 150:
            call = True
        else:
            fold = True
        return call, fold, raise_bet

    def _five_cards_call(self, call, card_value, fold, raise_bet):
        if card_value > 200:
            raise_bet = True
        elif card_value >= 110:
            call = True
        else:
            fold = True
        return call, fold, raise_bet

    def _two_cards_call(self, call, card_value, fold, raise_bet):
        if card_value > 200:
            raise_bet = True
        elif card_value >= 105:
            call = True
        else:
            fold = True
        return call, fold, raise_bet

    def _print_call_thought(self, all_in, call, fold, raise_bet):
        if raise_bet:
            print(f"{self.player.name} thinks they should raise")
        if call:
            print(f"{self.player.name} thinks they should call")
        if all_in:
            print(f"{self.player.name} thinks they should go all in")
        if fold:
            print(f"{self.player.name} thinks they should fold")
