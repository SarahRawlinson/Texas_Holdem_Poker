class Player:
    def __init__(self, name, hand, controller=None):
        self._name = name
        self._hand = hand
        self._chips = 0
        self._active = True
        self.controller = controller
        self._starting_cards = hand.cards

    def __repr__(self):
        return self._name

    def best_hand(self):
        return self._hand.hand

    def _get_name(self):
        return self._name

    def _get_hand(self):
        return self._hand

    def _set_hand(self, hand):
        if len(self._hand.cards) == 0:
            self._starting_cards = hand
        self._hand.add_cards(hand)

    def remove_cards(self):
        self._hand.remove_cards()
        cards = self._starting_cards.copy()
        self._starting_cards = []
        return cards

    def fold(self):
        print(f"{self._name} folds!")
        self._active = False

    def _return_active(self):
        return self._active

    def _set_active(self, active):
        self._active = active

    def add_chips(self, amount):
        self._chips += amount

    def remove_chips(self, amount):
        print(f"{self._name} add {amount} chips to the pot")
        self._chips = self._chips - amount

    def _get_chips(self):
        return self._chips

    def bet(self, amount):
        self.remove_chips(amount)
        return amount

    def next_action(self, bet, total_bet):
        if self.controller is None:
            return 0
        if bet == 0:
            return self.check_for_bet(bet, total_bet)
        elif bet > 0:
            self.controller.check_for_call(bet, total_bet)
            if self.controller.fold:
                self.fold()
                return 0
            else:
                if self.controller.raise_bet:
                    new_bet = self.check_for_bet(bet, total_bet)
                    return new_bet + bet
                else:
                    return bet

    def check_for_bet(self, bet, total_bet):
        self.controller.make_decision(bet, total_bet)
        if self.controller.wants_to_bet:
            chips = self.controller.bet_qty
            return chips
        else:
            return 0

    def _get_starting_hand(self):
        cards_as_strings = [str(card) for card in self._starting_cards]
        return ", ".join(cards_as_strings)

    name = property(_get_name)
    hand = property(_get_hand, _set_hand)
    active = property(_return_active, _set_active)
    chips = property(_get_chips)
    two_cards = property(_get_starting_hand)
