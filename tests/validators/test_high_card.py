import unittest
from poker.validators import HighCard
from poker.card import Card


class TestHighCard(unittest.TestCase):
    def test_hand_return_valid(self):
        hand = [
            Card("7", "Diamonds"),
            Card("Ace", "Diamonds")
        ]
        validator = HighCard(hand)
        self.assertEqual(validator.is_valid, True)

    def test_hand_return_high_card(self):
        card_7d = Card("7", "Diamonds")
        card_ad = Card("Ace", "Diamonds")
        card_7h = Card("7", "Hearts")
        card_kh = Card("King", "Hearts")
        card_qh = Card("Queen", "Hearts")
        hand = [
            card_7d,
            card_ad
        ]
        validator = HighCard(hand)
        self.assertEqual(validator.high_card, [card_ad])

    def test_hand_return_name(self):
        hand = [
            Card("7", "Diamonds"),
            Card("Ace", "Diamonds")
        ]
        validator = HighCard(hand)
        self.assertEqual(validator.name, "High Card")
