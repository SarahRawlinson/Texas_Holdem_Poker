from poker.card import Card
from poker.card_deck import CardDeck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound
from poker.ai import AI

# from main import deck, cards, hand1, hand2, player1, player2

deck = CardDeck()
cards = Card.create_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()
hand3 = Hand()
hand4 = Hand()
hand5 = Hand()

player1 = Player("Sarah", hand1)
player2 = Player("Mark", hand2)
player3 = Player("Steven", hand3)
player4 = Player("Barry", hand4)
player5 = Player("Boris", hand5)

ai1 = AI(player=player1)
ai2 = AI(player=player2)
ai3 = AI(player=player3)
ai4 = AI(player=player4)
ai5 = AI(player=player5)

players = [player1, player2, player3, player4]

for player in players:
    player.add_chips(1000)

game = GameRound(players=players, deck=deck)
# game.set_game_qty(game_qty=10)
game.set_game_qty(infinite=True)
game.play()


