import unittest
from unittest.mock import MagicMock, call
from poker.game_round import GameRound
from poker.card_deck import CardDeck
from poker.card import Card
from poker.player import Player
from poker.hand import Hand
from poker.ai import AI

#
# class TestGameRound(unittest.TestCase):
#
#     hand1 = Hand()
#     player1 = Player("Sarah", hand1)
#     ai1 = AI(player1)
#     hand2 = Hand()
#     player2 = Player("Bob", hand2)
#     ai2 = AI(player2)
#     cards = Card.create_cards()
#     deck = CardDeck()
#
#     def test_game_round_stores_deck_and_players(self):
#         deck = self.deck
#         deck.add_cards(self.cards)
#         players = [self.player1, self.player2]
#         game_round = GameRound(deck=deck, players=players)
#         self.assertEqual(game_round.players, players)
#         self.assertEqual(game_round.deck, deck)
#
#     def test_game_round_shuffles(self):
#         deck = self.deck
#         players = [self.player1, self.player2]
#
#         game_round = GameRound(deck=deck, players=players)
#         game_round.play()
#         deck.shuffle.assert_called_once()
#
#     def test_game_deals_players(self):
#         deck = self.deck
#         players = [self.player1, self.player2]
#         game_round = GameRound(deck=deck, players=players)
#         game_round.play()
#         deck.deal_cards.assert_has_calls([call(2), call(2)])
#
#     def test_check_for_active_players(self):
#         deck = self.deck
#         players = [self.player1, self.player2]
#         game_round = GameRound(deck=deck, players=players)
#         return_players = game_round.check_for_active_players()
#         self.assertEqual(return_players, players)
#         self.player1.active = False
#         return_players = game_round.check_for_active_players()
#         self.assertEqual(return_players, [self.player2])
#
#     def test_check_for_inactive_players(self):
#         deck = self.deck
#         players = [self.player1, self.player2]
#         game_round = GameRound(deck=deck, players=players)
#         self.player1.active = False
#         return_players = game_round.check_for_inactive_players()
#         self.assertEqual(return_players, [self.player1])
#
#     def test_community_cards(self):
#         cards = Card.create_cards()
#         deck = CardDeck()
#         deck.add_cards(cards)
#         players = [self.player1]
#         game_round = GameRound(deck=deck, players=players)
#         game_round.play()
#         self.assertEqual(len(game_round.community_cards), 5)
#         self.assertEqual(len(self.player1.hand.cards), 7)
#
#     def test_community_pot(self):
#         deck = self.deck
#         self.player1.add_chips(50)
#         players = [self.player1]
#         game_round = GameRound(deck=deck, players=players)
#         game_round.bet(self.player1, 20)
#         self.assertEqual(game_round.community_pot, 20)
# #
