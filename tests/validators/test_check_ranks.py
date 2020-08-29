import unittest
from poker.validators import CheckRanksAndSuits as CheckRanks
from poker.card import Card


class TestCheckRanks(unittest.TestCase):
    card_a = Card("8", "Clubs")
    card_b = Card("8", "Hearts")
    card_c = Card("10", "Clubs")
    card_d = Card("10", "Hearts")
    card_e = Card("Ace", "Clubs")
    card_f = Card("Ace", "Hearts")
    card_g = Card("Ace", "Diamonds")
    card_h = Card("King", "Clubs")
    card_i = Card("Queen", "Clubs")

    def test_pair(self):
        cards = [self.card_a, self.card_b]
        ranks = CheckRanks(cards)
        self.assertEqual(ranks.list_ranks, {"8": {"cards": cards, "value": 7}})

    def test_high(self):
        cards = [self.card_e, self.card_b]
        ranks = CheckRanks(cards)
        self.assertEqual(ranks.list_ranks, {"Ace": {"cards": [self.card_e], "value": 13},
                                            "8": {"cards": [self.card_b], "value": 7}})
