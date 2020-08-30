import unittest
from unittest.mock import MagicMock
from poker.ai import AI
from poker.player import Player
from poker.hand import Hand
from poker.card import Card


# class TestAI(unittest.TestCase):
#     def test_ai_bet(self):
#         cards = [Card("Ace", "Spades"), Card("3", "Spades")]
#         hand = Hand(cards)
#         player = Player("AI", hand, controller=MagicMock())
#         player.add_chips(80)
#         ai = AI(player)
#         ai.make_decision()
#         self.assertEqual(player.hand.value, 13)
#         # AI now randomized test no longer valid
#         # self.assertEqual(ai.wants_to_bet, True)
#         ai.check_for_call(10)
#         self.assertEqual(ai.call, True)
