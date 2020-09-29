class HighCard:

    def __init__(self, hand):
        self._hand = hand
        self._name = "High Card"
        self._hand.sort(reverse=True)
        pass

    def _is_valid(self):
        return len(self._hand) > 0

    def _high_card(self):
        return self._hand[:1]

    def _get_name(self):
        return self._name

    def _high_card_value(self):
        return self._hand[0].value

    is_valid = property(_is_valid)
    cards = property(_high_card)
    high_card = property(_high_card)
    name = property(_get_name)
    value = property(_high_card_value)
