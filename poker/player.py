class Player:
    def __init__(self, name, hand):
        self._name = name
        self._hand = hand
        self._chips = "0"

    def best_hand(self):
        return self._hand.hand

    def _get_name(self):
        return self._name

    def _get_hand(self):
        return self._hand

    def _set_hand(self, hand):
        self._hand.add_cards(hand)

    name = property(_get_name)
    hand = property(_get_hand, _set_hand)
