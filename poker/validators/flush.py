class Flush:
    def __init__(self, hand):
        self._is_valid = False
        self._flush_cards = []
        self._flush_suit = "None"
        self._flush_value = 0
        if len(hand) >= 5:
            suits = {}
            for card in hand:
                suits.setdefault(card.suit, [])
                suits[card.suit].append(card)
            for suit in suits:
                cards = suits[suit]
                cards.sort(reverse=True)
                if len(cards) == 5:
                    self._set_flush(suit, cards)

                elif len(cards) > 5:
                    self._set_flush(suit, cards[:5])

    def _set_flush(self, suit, cards):
        self._is_valid = True
        self._flush_cards = cards
        self._flush_suit = suit
        self._set_flush_value()

    def _set_flush_value(self):
        value = 0
        for card in self._flush_cards:
            value += card.value
        self._flush_value = value

    def _get_value(self):
        return self._flush_value

    def _get_is_valid(self):
        return self._is_valid

    def _get_flush_cards(self):
        return self._flush_cards

    is_valid = property(_get_is_valid)
    cards = property(_get_flush_cards)
    value = property(_get_value)
