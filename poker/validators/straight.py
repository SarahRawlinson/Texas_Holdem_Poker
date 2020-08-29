from poker.validators import CheckRanksAndSuits as Checker


class Straight:
    def __init__(self, ranks, suits):
        self._is_valid = False
        self._straight_cards = []
        self._multiple_straight = False
        self._high_straight = []
        self._flush_straight = []
        self._value = 0
        self._workout_straight_from_ranks(ranks)
        if len(self._straight_cards) != 5 and self._is_valid:
            self._high_straight = self._high_straight[:5]
            self._multiple_straight = True
            self._check_suit(suits)
        self._work_out_value()

    def _workout_straight_from_ranks(self, ranks):
        last_value = 0
        straight = 0
        straight_cards = []
        high_straight = []
        for rank in ranks:
            list_card = ranks[rank]["cards"][0]
            if last_value > 0 and (last_value - 1) == ranks[rank]["value"]:
                straight += 1
                straight_cards.extend(ranks[rank]["cards"])
                high_straight.append(list_card)
                if straight >= 5:
                    self._is_valid = True
                    self._straight_cards = straight_cards
                    self._high_straight = high_straight
            else:
                straight = 1
                straight_cards = []
                high_straight = []
                straight_cards.extend(ranks[rank]["cards"])
                high_straight.append(list_card)
            last_value = ranks[rank]["value"]

    def _check_suit(self, suits):
        valid_straight = []
        for cards in suits:
            check = Checker(suits[cards]["cards"])
            straight = Straight(check.list_ranks, check.list_suits)
            if straight._is_valid:
                valid_straight = straight.high_straight
        if len(valid_straight) == 5:
            self._flush_straight = valid_straight
            self._high_straight = valid_straight

    def _get_is_valid(self):
        return self._is_valid

    def _get_high_straight(self):
        return self._high_straight

    def _get_value(self):
        return self._value

    def _work_out_value(self):
        value = 0
        for card in self._high_straight:
            value += card.value
        self._value = value

    is_valid = property(_get_is_valid)
    high_straight = property(_get_high_straight)
    value = property(_get_value)
    cards = property(_get_high_straight)


