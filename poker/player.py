class Player:
    def __init__(self, name, hand):
        self._name = name
        self._hand = hand
        self._chips = 0
        self._active = True

    def best_hand(self):
        return self._hand.hand

    def _get_name(self):
        return self._name

    def _get_hand(self):
        return self._hand

    def _set_hand(self, hand):
        self._hand.add_cards(hand)

    def fold(self):
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

    name = property(_get_name)
    hand = property(_get_hand, _set_hand)
    active = property(_return_active, _set_active)
    chips = property(_get_chips)
