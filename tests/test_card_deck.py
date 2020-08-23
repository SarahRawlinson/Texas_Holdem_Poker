import unittest
from poker.card_deck import Card_Deck
from poker.card import Card


class Test_Card_Deck(unittest.TestCase):
    def test_card_deck_no_cards_at_start(self):
        card_deck = Card_Deck()
        self.assertEqual(card_deck.cards, [])

    def test_cards_added(self):
        card_deck = Card_Deck()
        cards = [Card("7", "Hearts"), Card("8", "Hearts")]
        card_deck.add_cards(cards)
        print(card_deck.cards)
        self.assertEqual(card_deck.cards, cards)
