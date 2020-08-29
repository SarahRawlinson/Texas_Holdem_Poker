class CheckRanksAndSuits:
    def __init__(self, hand):
        self._hand = hand
        self._cards_by_rank = []
        self._cards_by_suit = []
        self._order_cards_by_rank()

    def _order_cards_by_rank(self):
        rank_dic = {}
        suit_dic = {}
        self._hand.sort(reverse=True)
        for card in self._hand:
            rank_dic.setdefault(card.rank, {"cards": list(), "value": card.value})
            rank_dic[card.rank]["cards"].append(card)
            suit_dic.setdefault(card.suit, {"cards": list(), "value": card.value})
            suit_dic[card.suit]["cards"].append(card)
        self._cards_by_rank = rank_dic
        self._cards_by_suit = suit_dic

    def _return_rank_dictionary(self):
        return self._cards_by_rank

    def _return_suit_dictionary(self):
        return self._cards_by_suit

    list_ranks = property(_return_rank_dictionary)
    list_suits = property(_return_suit_dictionary)
