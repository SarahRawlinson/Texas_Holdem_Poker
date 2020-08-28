import unittest
from unittest.mock import patch
from poker.card_deck import CardDeck
from poker.card import Card


class TestCardDeck(unittest.TestCase):
    def test_card_deck_no_cards_at_start(self):
        card_deck = CardDeck()
        self.assertEqual(card_deck.cards, [])

    def test_cards_added(self):
        card_deck = CardDeck()
        cards = [Card("7", "Hearts"), Card("8", "Hearts")]
        card_deck.add_cards(cards)
        self.assertEqual(card_deck.cards, cards)

    @patch('random.shuffle')
    def test_deck_shuffle(self, mock_shuffle):
        card_deck = CardDeck()
        cards = [Card("7", "Hearts"), Card("8", "Hearts")]
        card_deck.add_cards(cards)
        card_deck.shuffle()
        mock_shuffle.assert_called_once_with(cards)

    def test_deal(self):
        card_deck = CardDeck()
        cards = Card.create_cards()
        card_deck.add_cards(cards)
        cards_a = card_deck.deal_cards(2)
        cards_b = cards[:2]
        self.assertEqual(cards_a, cards_b)
        cards_a = card_deck.cards
        del cards[:2]
        cards_b = cards
        self.assertEqual(cards_a, cards_b)
