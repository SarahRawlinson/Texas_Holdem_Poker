class Duplicated:
    def __init__(self, hand, amount):
        self._hand = hand
        if len(self._hand) == amount:
            self._is_valid = True
            self._value = self._work_out_value()
        else:
            self._is_valid = False
            self._value = 0

    def _is_valid(self):
        return self._is_valid

    def _get_value(self):
        return self._value

    def _work_out_value(self):
        value = 0
        for card in self._hand:
            value += card.value
        return value

    is_valid = property(_is_valid)
    value = property(_get_value)
