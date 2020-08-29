import unittest
from poker.validators import Straight
from poker.validators import CheckRanksAndSuits as CheckRanks
from poker.card import Card


class TestStraight(unittest.TestCase):
    def test_straight(self):
        hand = [
            Card("2", "Clubs"),
            Card("3", "Diamonds"),
            Card("4", "Hearts"),
            Card("5", "Diamonds"),
            Card("6", "Diamonds")
        ]
        ranks = CheckRanks(hand)
        straight = Straight(ranks.list_ranks, ranks.list_suits)
        self.assertEqual(straight.is_valid, True)

    def test_straight_and_extra(self):
        hand = [
            Card("2", "Clubs"),
            Card("3", "Diamonds"),
            Card("4", "Hearts"),
            Card("5", "Diamonds"),
            Card("Queen", "Diamonds"),
            Card("Ace", "Diamonds"),
            Card("6", "Diamonds")
        ]
        ranks = CheckRanks(hand)
        straight = Straight(ranks.list_ranks, ranks.list_suits)
        self.assertEqual(straight.is_valid, True)

    def test_not_straight(self):
        hand = [
            Card("2", "Clubs"),
            Card("3", "Diamonds"),
            Card("4", "Hearts"),
            Card("5", "Diamonds")
        ]
        ranks = CheckRanks(hand)
        straight = Straight(ranks.list_ranks, ranks.list_suits)
        self.assertEqual(straight.is_valid, False)

    def test_not_straight2(self):
        hand = [
            Card("2", "Clubs"),
            Card("3", "Diamonds"),
            Card("4", "Hearts"),
            Card("5", "Diamonds"),
            Card("5", "Diamonds"),
        ]
        ranks = CheckRanks(hand)
        straight = Straight(ranks.list_ranks, ranks.list_suits)
        self.assertEqual(straight.is_valid, False)

    def test_not_straight_value(self):
        hand = [
            Card("2", "Clubs"),
            Card("3", "Diamonds"),
            Card("4", "Hearts"),
            Card("5", "Diamonds"),
            Card("6", "Diamonds"),
        ]
        ranks = CheckRanks(hand)
        straight = Straight(ranks.list_ranks, ranks.list_suits)
        self.assertEqual(straight.value, 15)

    def test_straight_flush_return(self):
        hand = [
            Card("2", "Diamonds"),
            Card("3", "Diamonds"),
            Card("4", "Diamonds"),
            Card("5", "Diamonds"),
            Card("7", "Clubs"),
            Card("8", "Clubs"),
            Card("6", "Diamonds"),
        ]
        expected_hand = [
            Card("6", "Diamonds"),
            Card("5", "Diamonds"),
            Card("4", "Diamonds"),
            Card("3", "Diamonds"),
            Card("2", "Diamonds"),
        ]
        ranks = CheckRanks(hand)
        straight = Straight(ranks.list_ranks, ranks.list_suits)
        self.assertEqual(straight.high_straight, expected_hand)

    def test_straight_return_higher(self):
        hand = [
            Card("9", "Diamonds"),
            Card("3", "Diamonds"),
            Card("4", "Diamonds"),
            Card("5", "Diamonds"),
            Card("7", "Clubs"),
            Card("8", "Clubs"),
            Card("6", "Diamonds"),
        ]
        expected_hand = [
            Card("9", "Diamonds"),
            Card("5", "Diamonds"),
            Card("7", "Clubs"),
            Card("8", "Clubs"),
            Card("6", "Diamonds"),
        ]
        expected_hand.sort(reverse=True)
        ranks = CheckRanks(hand)
        straight = Straight(ranks.list_ranks, ranks.list_suits)
        self.assertEqual(straight.high_straight, expected_hand)