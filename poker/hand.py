class Hand:
    def __init__(self, cards=None):
        self._set_up_hand(cards)

    def _set_up_hand(self, cards):
        if cards is not None:
            self.cards = cards
            self.__hand__()
        else:
            self.cards = []
            self._hand = "No Hand"
            self._value = 0

    def add_cards(self, cards):
        self.cards.extend(cards)
        self.__hand__()

    def remove_cards(self):
        self._set_up_hand(cards=None)

    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def __high_card_value__(self):
        value = 0
        for card in self.cards:
            if card.value > value:
                value = card.value
        return value

    def __hand__(self):
        hands, values = self._check_hands()
        hand = "High Card"
        hands[hand]["score"] = self.high_card_value
        for hand_name in reversed(hands):
            if hands[hand_name]["is true"]:
                hand = hand_name
                break
        self._hand = hand
        self._value = ((hands[hand]["value"] ** hands[hand]["value"]) * hands[hand]["score"]) + sum(values)

    def _return_hand(self):
        return self._hand

    def _return_value(self):
        return self._value

    @property
    def _card_values(self):
        ranks = {}
        suits = {}
        values = []
        self.cards.sort(reverse=True)
        for card in self.cards:
            dic = {"number": 0, "value": 0}
            ranks.setdefault(card.rank, dic)
            ranks[card.rank]["number"] += 1
            ranks[card.rank]["value"] += card.value
            suits.setdefault(card.suit, 0)
            suits[card.suit] += 1
            values.append(card.value)

        return [ranks, suits, values]

    @property
    def _hand_dictionary(self):
        hands = {
            "High Card": {"is true": True, "value": 10, "score": 0},
            "Pair": {"is true": False, "value": 20, "score": 0},
            "Two Pair": {"is true": False, "value": 30, "score": 0},
            "Three of a Kind": {"is true": False, "value": 40, "score": 0},
            "Straight": {"is true": False, "value": 50, "score": 0},
            "Flush": {"is true": False, "value": 60, "score": 0},
            "Full House": {"is true": False, "value": 70, "score": 0},
            "Four of a Kind": {"is true": False, "value": 80, "score": 0},
            "Straight Flush": {"is true": False, "value": 90, "score": 0},
            "Royal Flush": {"is true": False, "value": 100, "score": 0}
        }
        return hands

    @staticmethod
    def _check_ranks(ranks, hands):
        for rank in ranks:
            if ranks[rank]["number"] == 2:
                if hands["Pair"]["is true"]:
                    if not hands["Two Pair"]["is true"]:
                        hands["Two Pair"]["is true"] = True
                        hands["Two Pair"]["score"] = ranks[rank]["value"] + hands["Pair"]["score"]
                else:
                    hands["Pair"]["is true"] = True
                    hands["Pair"]["score"] = ranks[rank]["value"]

            elif ranks[rank]["number"] == 3 and not hands["Three of a Kind"]["is true"]:
                hands["Three of a Kind"]["is true"] = True
                hands["Three of a Kind"]["score"] = ranks[rank]["value"]

            elif ranks[rank]["number"] == 4:
                hands["Four of a Kind"]["is true"] = True
                hands["Four of a Kind"]["score"] = ranks[rank]["value"]
        return hands

    @staticmethod
    def _check_for_straight(values, hands):

        last_value = 0
        hands["Straight"]["is true"] = True
        hands["Straight"]["score"] = sum(values)
        for value in values:
            if last_value != 0:
                if last_value + 1 != value:
                    hands["Straight"]["is true"] = False
                    hands["Straight"]["score"] = 0
                    break
            last_value = value
        return hands

    @staticmethod
    def _check_suits(suits, hands, values):
        for suit in suits:
            if suits[suit] == 5:
                hands["Flush"]["is true"] = True
                hands["Flush"]["score"] = sum(values)
                if hands["Straight"]["is true"]:
                    hands["Straight Flush"]["is true"] = True
                    hands["Straight Flush"]["score"] = sum(values)
                    if values[4] == 13:
                        hands["Royal Flush"]["is true"] = True
                        hands["Royal Flush"]["score"] = sum(values)
            else:
                break
        return hands

    @staticmethod
    def _check_full_house(hands):
        if hands["Pair"]["is true"] and hands["Three of a Kind"]["is true"]:
            hands["Full House"]["is true"] = True
            hands["Full House"]["score"] = hands["Pair"]["score"] + hands["Three of a Kind"]["score"]
        return hands

    def _check_hands(self):
        hands = self._hand_dictionary
        ranks, suits, values = self._card_values

        if len(self.cards) >= 5:
            values.sort()

            hands = self._check_for_straight(values, hands)

            hands = self._check_suits(suits, hands, values)

            if not hands["Straight"]["is true"]:
                hands = self._check_ranks(ranks, hands)

                hands = self._check_full_house(hands)
        else:
            hands = self._check_ranks(ranks, hands)
        return [hands, values]

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.hand == other.hand and self.value == other.value

    high_card_value = property(__high_card_value__)
    hand = property(_return_hand)
    value = property(_return_value)
