from poker.validators import HighCard
from poker.validators import CheckRanksAndSuits as CheckRanks
from poker.validators import Duplicated
from poker.validators import Flush
from poker.validators import Straight


class Hand:

    def __init__(self, cards=None):
        self._set_up_hand(cards)
        self._hand_dictionary = self.__hand_dictionary

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.hand == other.hand and self.score == other.score

    def __repr__(self):
        cards_as_strings = [str(card) for card in self._cards]
        return ", ".join(cards_as_strings)

    def add_cards(self, cards):
        self._cards.extend(cards)
        self._hand_dictionary = self.__hand_dictionary
        self.__hand__()

    def remove_cards(self):
        self._set_up_hand(cards=None)

    def _set_up_hand(self, cards):
        self._hand_dictionary = self.__hand_dictionary        
        self._hand = "No Hand"
        self._score = 0
        self._hand_cards_value = 0
        self._hand_cards = []
        if cards is not None:
            self._cards = cards
            self.__hand__()
        else:
            self._cards = []
            
    def __hand__(self):
        hands = self._hand_dictionary
        self._check_hands()

        for hand_name in reversed(hands):
            if hands[hand_name]["is true"]:
                self._hand = hand_name
                break
        self._hand_cards_value = self._get_hand_value(self._hand)
        hand = self._hand
        self._score = ((hands[hand]["value"] ** hands[hand]["value"]) * hands[hand]["score"])
        self._hand_cards = hands[hand]["cards"]

    def _check_hands(self):
        check = CheckRanks(self._cards)
        ranks = check.list_ranks
        suits = check.list_suits
        self._check_high_score()
        for rank in ranks:
            self._check_pairs(ranks[rank]["cards"])
            self._check_three_of_kind(ranks[rank]["cards"])
            self._check_four_of_kind(ranks[rank]["cards"])
        self._check_full_house()
        self._check_for_flush(self._cards)
        self._check_for_straight(ranks, suits)
        self._check_for_straight_flush()
        self._check_for_royal_flush()

    def _set_hand(self, hand, value, cards):
        hands = self._hand_dictionary
        hands[hand]["is true"] = True
        hands[hand]["score"] = value
        hands[hand]["cards"] = cards

    def _get_hand_value(self, hand):
        return self._hand_dictionary[hand]["score"]

    def _hand_true(self, hand):
        return self._hand_dictionary[hand]["is true"]

    def _get_hand_cards(self, hand):
        return self._hand_dictionary[hand]["cards"]

    def _check_high_score(self):
        high_card = HighCard(self._cards)
        if high_card.is_valid:
            self._set_hand("High Card", high_card.value, high_card.high_card)

    def _check_pairs(self, cards):
        pair = Duplicated(cards, 2)
        if pair.is_valid:
            if self._hand_true("Pair"):
                self._set_hand("Two Pair", pair.value + self._get_hand_value("Pair"),
                               pair.cards + self._get_hand_cards("Pair"))
            else:
                self._set_hand("Pair", pair.value, pair.cards)

    def _check_three_of_kind(self, cards):
        three = Duplicated(cards, 3)
        if three.value > self._get_hand_value("Three of a Kind"):
            self._set_hand("Three of a Kind", three.value, cards)

    def _check_four_of_kind(self, cards):
        four = Duplicated(cards, 4)
        if four.value > self._get_hand_value("Four of a Kind"):
            self._set_hand("Four of a Kind", four.value, cards)

    def _check_full_house(self):
        if self._hand_true("Pair") and self._hand_true("Three of a Kind"):
            value = self._get_hand_value("Pair") + self._get_hand_value("Two Pair")
            cards = self._get_hand_cards("Pair") + self._get_hand_cards("Two Pair")
            self._set_hand("Full House", value, cards)

    def _check_for_flush(self, cards):
        flush = Flush(cards)
        if flush.is_valid:
            self._set_hand("Flush", flush.value, flush.cards)

    def _check_for_straight(self, ranks, suits):
        straight = Straight(ranks, suits)
        if straight.is_valid:
            self._set_hand("Straight", straight.value, straight.cards)

    def _check_for_straight_flush(self):
        if self._hand_true("Straight") and self._hand_true("Flush"):
            straight_flush = Flush(self._get_hand_cards("Straight"))
            if straight_flush.is_valid:
                self._set_hand("Straight Flush", straight_flush.value, straight_flush.cards)

    def _check_for_royal_flush(self):
        if self._hand_true("Straight Flush"):
            if self._get_hand_cards("Straight Flush")[0].value == 13:
                self._set_hand("Royal Flush", self._get_hand_value("Straight Flush"),
                               self._get_hand_cards("Straight Flush"))

    def _return_hand(self):
        return self._hand

    def _return_score(self):
        return self._score

    def _return_value(self):
        return self._hand_cards_value

    def _return_cards(self):
        return self._cards

    def _return_hand_cards(self):
        cards_as_strings = [str(card) for card in self._hand_cards]
        return ", ".join(cards_as_strings)

    @property
    def __hand_dictionary(self):
        hands = {
            "High Card": {"is true": True, "value": 10, "score": 0, "cards": []},
            "Pair": {"is true": False, "value": 20, "score": 0, "cards": []},
            "Two Pair": {"is true": False, "value": 30, "score": 0, "cards": []},
            "Three of a Kind": {"is true": False, "value": 40, "score": 0, "cards": []},
            "Straight": {"is true": False, "value": 50, "score": 0, "cards": []},
            "Flush": {"is true": False, "value": 60, "score": 0, "cards": []},
            "Full House": {"is true": False, "value": 70, "score": 0, "cards": []},
            "Four of a Kind": {"is true": False, "value": 80, "score": 0, "cards": []},
            "Straight Flush": {"is true": False, "value": 90, "score": 0, "cards": []},
            "Royal Flush": {"is true": False, "value": 100, "score": 0, "cards": []}
        }
        return hands

    hand = property(_return_hand)
    score = property(_return_score)
    value = property(_return_value)
    cards = property(_return_cards)
    hand_cards = property(_return_hand_cards)

