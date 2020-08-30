class Player:
    def __init__(self, name, hand, controller=None):
        self._name = name
        self._hand = hand
        self._chips = 0
        self._active = True
        self.controller = controller

    def best_hand(self):
        return self._hand.hand

    def _get_name(self):
        return self._name

    def _get_hand(self):
        return self._hand

    def _set_hand(self, hand):
        self._hand.add_cards(hand)

    def fold(self):
        print(f"{self.name} folds!")
        self._active = False

    def _return_active(self):
        return self._active

    def _set_active(self, active):
        self._active = active

    def remove_cards(self):
        self._hand.remove_cards()

    def add_chips(self, amount):
        self._chips += amount

    def remove_chips(self, amount):
        self._chips -= amount

    def _get_chips(self):
        return self._chips

    def bet(self, amount):
        self.remove_chips(amount)
        return amount

    def next_action(self, game_responce, bet):
        if self.controller is None:
            return 0
        if game_responce == "check":
            return self.check_for_bet(0)
        elif game_responce == "call":
            self.controller.check_for_call(bet)
            if self.controller.fold:
                self.fold()
                return 0
            else:
                if self.controller.raise_bet:
                    new_bet = self.check_for_bet(bet)
                    # if new_bet > 0:
                        # print(f"{self.name} raises {new_bet}")
                    # else:
                        # print(f"{self.name} calls")
                    return new_bet + bet
                else:
                    # print(f"{self.name} calls")
                    self.bet(bet)
                    return bet

    def check_for_bet(self, bet):
        self.controller.make_decision(bet)
        if self.controller.wants_to_bet:
            chips = self.controller.bet_qty
            self.bet(chips + bet)
            return chips
        else:
            return 0

    name = property(_get_name)
    hand = property(_get_hand, _set_hand)
    active = property(_return_active, _set_active)
    chips = property(_get_chips)
