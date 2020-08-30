import random


class AI:
    def __init__(self, player):
        self.fold = False
        self.player = player
        self.wants_to_bet = False
        self.check = True
        self.call = True
        self.bet_qty = 0
        self.all_in = False
        self.raise_bet = False
        player.controller = self

    def make_decision(self, bet):
        if bet > 0:
            self.check_for_call(bet)
        else:
            wants_to_bluff = False
            if self.player.chips > 50 and self.player.hand.value >= 7:
                self.wants_to_bet = True
                self.bet()
                self.check = False
                wants_to_bluff = random.choice([True, False])
            else:
                self.wants_to_bet = False
                self.check = True
            if wants_to_bluff:
                self.bluff()

    def bet(self):
        card_amount = len(self.player.hand.cards)
        card_value = self.player.hand.value
        if card_amount == 2:
            if card_value > 13:
                amount_to_bet = 10
            elif card_value > 20:
                amount_to_bet = 30
            else:
                amount_to_bet = 5
        elif card_amount == 5:
            if card_value > 20:
                amount_to_bet = 10
            elif card_value > 30:
                amount_to_bet = 30
            else:
                amount_to_bet = 5
        elif card_amount == 6:
            if card_value > 25:
                amount_to_bet = 10
            elif card_value > 30:
                amount_to_bet = 30
            else:
                amount_to_bet = 2
        elif card_amount == 7:
            if card_value > 30:
                amount_to_bet = 20
            elif card_value > 40:
                amount_to_bet = 30
            else:
                amount_to_bet = 2
        else:
            amount_to_bet = 2
        self.bet_qty = amount_to_bet

    def bluff(self):
        random_choice = random.choice([0, 1, 2, 3, 4, 5])
        self.try_function(random_choice)

    def check_for_call(self, amount):
        card_amount = len(self.player.hand.cards)
        card_value = self.player.hand.value
        call = False
        raise_bet = False
        all_in = False
        fold = False
        if self.player.chips > amount:
            if card_amount == 2:
                if card_value >= 13:
                    call = True
            elif card_amount == 5:
                if card_value >= 15:
                    call = True
            elif card_amount == 6:
                if card_value >= 18:
                    call = True
            elif card_amount == 7:
                if card_value >= 22:
                    call = True
            if card_value >= 30:
                raise_bet = True
        else:
            if card_value >= 30:
                all_in = True
            else:
                fold = True
        self.call = call
        self.all_in = all_in
        self.raise_bet = raise_bet
        self.fold = fold

    def drop_bet(self):
        self.bet_qty = 0
        self.wants_to_bet = False

    def no_change(self):
        pass

    def change_top_bet(self):
        self.bet_qty = 30
        self.wants_to_bet = True

    def change_high_bet(self):
        self.bet_qty = 20
        self.wants_to_bet = True

    def change_low_bet(self):
        self.bet_qty = 2
        self.wants_to_bet = True

    def change_med_bet(self):
        self.bet_qty = 5
        self.wants_to_bet = True

    def try_function(self, args):
        get_function = {0: self.drop_bet,
                        1: self.no_change,
                        2: self.change_top_bet,
                        3: self.change_high_bet,
                        4: self.change_med_bet,
                        5: self.change_low_bet}
        func = get_function.get(int(args), "nothing")
        return func()
