import unittest
from poker.validators import Duplicated
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
        pair = Duplicated(cards, 2)
        self.assertEqual(pair.is_valid, True)

    def test_pair_value(self):
        cards = [self.card_a, self.card_b]
        pair = Duplicated(cards, 2)
        self.assertEqual(pair.value, 14)

    def test_three_of_kind(self):
        cards = [self.card_e, self.card_f, self.card_g]
        three_of_kind = Duplicated(cards, 3)
        self.assertEqual(three_of_kind.is_valid, True)

    def test_three_of_kind_value(self):
        cards = [self.card_e, self.card_f, self.card_g]
        three_of_kind = Duplicated(cards, 3)
        self.assertEqual(three_of_kind.value, 39)