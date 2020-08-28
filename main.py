from poker.card import Card
from poker.card_deck import CardDeck
from poker.hand import Hand
from poker.player import Player

# from main import deck, cards, hand1, hand2, player1, player2

deck = CardDeck()
cards = Card.create_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player("Sarah", hand1)
player2 = Player("Sarah", hand1)
