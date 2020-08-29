import unittest
from poker.validators import Flush
from poker.card import Card


class TestFlush(unittest.TestCase):
    def test_flush(self):
        hand = [
            Card("2", "Diamonds"),
            Card("4", "Diamonds"),
            Card("6", "Diamonds"),
            Card("8", "Diamonds"),
            Card("10", "Diamonds")
        ]
        flush = Flush(hand)
        self.assertEqual(flush.is_valid, True)

    def test_not_flush(self):
        hand = [
            Card("2", "Diamonds"),
            Card("4", "Diamonds"),
            Card("6", "Diamonds"),
            Card("8", "Diamonds"),
            Card("10", "Hearts")
        ]
        flush = Flush(hand)
        self.assertEqual(flush.is_valid, False)

    def test_mixed_flush(self):
        hand = [
            Card("2", "Diamonds"),
            Card("4", "Diamonds"),
            Card("6", "Diamonds"),
            Card("8", "Diamonds"),
            Card("10", "Hearts"),
            Card("8", "Hearts"),
            Card("5", "Diamonds")
        ]
        flush = Flush(hand)
        self.assertEqual(flush.is_valid, True)

    def test_flush_cards_length(self):
        hand = [
            Card("2", "Diamonds"),
            Card("4", "Diamonds"),
            Card("6", "Diamonds"),
            Card("8", "Diamonds"),
            Card("10", "Diamonds"),
            Card("King", "Diamonds"),
            Card("Ace", "Diamonds")
        ]
        flush = Flush(hand)
        self.assertEqual(len(flush.cards), 5)

    def test_flush_return_cards(self):
        hand = [
            Card("2", "Diamonds"),
            Card("4", "Diamonds"),
            Card("6", "Diamonds"),
            Card("8", "Diamonds"),
            Card("10", "Diamonds"),
            Card("King", "Diamonds"),
            Card("Ace", "Diamonds")
        ]
        expected_return = [
            Card("Ace", "Diamonds"),
            Card("King", "Diamonds"),
            Card("10", "Diamonds"),
            Card("8", "Diamonds"),
            Card("6", "Diamonds")
        ]
        flush = Flush(hand)
        self.assertEqual(flush.cards, expected_return)