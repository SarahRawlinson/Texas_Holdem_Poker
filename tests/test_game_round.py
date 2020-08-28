import unittest
from unittest.mock import MagicMock, call
from poker.game_round import GameRound


class TestGameRound(unittest.TestCase):
    def test_game_round_stores_deck_and_players(self):
        deck = MagicMock()
        players = [MagicMock(), MagicMock()]
        game_round = GameRound(deck=deck, players=players)
        self.assertEqual(game_round.players, players)
        self.assertEqual(game_round.deck, deck)

    def test_game_round_shuffles(self):
        deck = MagicMock()
        players = [MagicMock(), MagicMock()]

        game_round = GameRound(deck=deck, players=players)
        game_round.play()
        deck.shuffle.assert_called_once()

    def test_game_deals_players(self):
        deck = MagicMock()
        players = [MagicMock(), MagicMock()]
        game_round = GameRound(deck=deck, players=players)
        game_round.play()
        deck.deal_cards.assert_has_calls([call(2), call(2)])

    def test_check_for_active_players(self):
        deck = MagicMock()
        player1 = MagicMock()
        player2 = MagicMock()
        players = [player1, player2]
        game_round = GameRound(deck=deck, players=players)
        return_players = game_round.check_for_active_players()
        self.assertEqual(return_players, players)
        player1.active = False
        return_players = game_round.check_for_active_players()
        self.assertEqual(return_players, [player2])

    def test_check_for_inactive_players(self):
        deck = MagicMock()
        player1 = MagicMock()
        player2 = MagicMock()
        players = [player1, player2]
        game_round = GameRound(deck=deck, players=players)
        player1.active = False
        return_players = game_round.check_for_inactive_players()
        self.assertEqual(return_players, [player1])

