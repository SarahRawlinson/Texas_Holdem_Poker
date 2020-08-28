import unittest
# from unittest.mock import MagicMock
from poker.player import Player
from poker.hand import Hand
from poker.card import Card


class PlayerTest(unittest.TestCase):
    def test_scores_name(self):
        hand = Hand()
        player = Player(name="Sarah", hand=hand)
        self.assertEqual(player.name, "Sarah")
        self.assertEqual(player.hand, hand)

    # def test_works_out_Mock_best_hand(self):
    #     hand = MagicMock()
    #     player = Player(name="Sarah", hand=hand)
    #     player.best_hand()
    #     hand.hand.assert_called()

    def test_works_out_best_hand(self):
        hand = Hand()
        player = Player(name="Sarah", hand=hand)
        player.best_hand()
        self.assertEqual(player.best_hand(), hand.hand)

    def test_set_hand(self):
        hand = Hand()
        player = Player(name="Sarah", hand=hand)
        cards = [Card("Ace", "Hearts"), Card("7", "Hearts")]
        player.hand = cards

        self.assertEqual(player.hand.cards, cards)
