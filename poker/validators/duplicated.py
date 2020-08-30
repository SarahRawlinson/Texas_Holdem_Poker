class Duplicated:
    def __init__(self, hand, amount):
        self._hand = hand
        if len(self._hand) == amount:
            self._is_valid = True
            self._value = self._work_out_value()
        else:
            self._is_valid = False
            self._value = 0
        self._check_valid()

    def _is_valid(self):
        return self._is_valid

    def _get_value(self):
        return self._value

    def _work_out_value(self):
        value = 0
        for card in self._hand:
            value += card.value
        return value

    def _check_valid(self):
        rank = self._hand[0].rank
        for card in self._hand:
            if rank != card.rank:
                self._is_valid = False

    def _return_cards(self):
        return self._hand

    is_valid = property(_is_valid)
    value = property(_get_value)
    cards = property(_return_cards)
