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

    def test_player_decide_dop_out(self):
        hand = Hand()
        player = Player(name="Sarah", hand=hand)
        player.fold()
        self.assertEqual(player.active, False)
        player.active = True
        self.assertEqual(player.active, True)
        
    def test_remove_cards(self):
        cards = [Card("Ace", "Hearts"), Card("7", "Hearts")]
        hand = Hand(cards)
        player = Player(name="Sarah", hand=hand)
        player.remove_cards()
        self.assertEqual(player.hand.cards, [])
        
    def test_player_add_chips(self):
        hand = Hand()
        player = Player("Sarah", hand)
        player.add_chips(20)
        self.assertEqual(player.chips, 20)

    def test_player_remove_chips(self):
        hand = Hand()
        player = Player("Sarah", hand)
        player.add_chips(40)
        player.remove_chips(20)
        self.assertEqual(player.chips, 20)

    def test_player_bet(self):
        hand = Hand()
        player = Player("Sarah", hand)
        player.add_chips(50)
        bet = player.bet(20)
        self.assertEqual(20, 20)
        self.assertEqual(player.chips, 30)

