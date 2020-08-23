import unittest
from poker.card import Card


class Test_Card(unittest.TestCase):
    def test_rank(self):
        card = Card(rank="Queen", suit="Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_suit(self):
        card = Card(rank="7", suit="Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_rank_isstring(self):
        card = Card(rank=8, suit="Diamonds")
        self.assertEqual(card.rank, "8")

    def test_return_isstring(self):
        card = Card(rank=5, suit="Spades")
        self.assertEqual(str(card), "5 of Spades")

    def test_has_representation(self):
        card = Card(rank=9, suit="Spades")
        self.assertEqual(repr(card), "Card('9', 'Spades')")

    def test_suit_options(self):
        self.assertEqual(Card.SUITS, ("Hearts", "Spades", "Diamonds", "Clubs"))

    def test_rank_options(self):
        self.assertEqual(Card.RANKS, ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"))

    def test_card_only_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank="Two", suit="Hearts")

    def test_card_only_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank="2", suit="Jack")