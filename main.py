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

player1 = Player("Sarah", hand1)
player2 = Player("Mark", hand2)
player3 = Player("Steven", hand3)
player4 = Player("Barry", hand4)

ai1 = AI(player=player1)
ai2 = AI(player=player2)
ai3 = AI(player=player3)
ai4 = AI(player=player4)

players = [player1, player2, player3, player4]

for player in players:
    player.add_chips(100)

game = GameRound(players=players, deck=deck)
game.play()

for player in players:
    print(f"player {player.name} had a {player.hand.hand} with a value of {player.hand.value}")
winner = game.find_winner()
if len(winner) == 1:
    winner = winner[0]
    print(f"The Winner is {winner.name} with a {winner.hand.hand}.\
    The winning cards where {winner.hand}.")
else:
    names = []
    for win in winner:
        names.append(win.name)

    print(f"Players Draw, winners are {names}")
