from poker.card import Card
from poker.card_deck import CardDeck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound
from poker.ai import AI
from poker.human_player import Human, is_number


# from main import deck, cards, hand1, hand2, player1, player2

deck = CardDeck()
cards = Card.create_cards()
deck.add_cards(cards)

players = []
waiting_for_response = True

while waiting_for_response:
    answer = input("how many players would you like?\n")
    if is_number(answer):
        if int(answer) > 5:
            print("too many players try again\n")
            continue
    else:
        print("answer not valid, try again\n")
        continue

    answer = int(answer)

    first_time = True
    players = []
    for i in range(answer):
        if first_time:
            print("please enter your name\n")
        else:
            print("enter a name for an opponent\n")
        names = input("enter a player name\n")
        hand = Hand()
        player = Player(names, hand)
        if first_time:
            controller = Human(player=player)
        else:
            controller = AI(player=player)
        players.append(player)
        first_time = False
    waiting_for_response = False

# hand2 = Hand()
# hand3 = Hand()
# hand4 = Hand()
# hand5 = Hand()
#
#
# player2 = Player("Mark", hand2)
# player3 = Player("Steven", hand3)
# player4 = Player("Barry", hand4)
# player5 = Player("Boris", hand5)
#
#
# ai2 = AI(player=player2)
# ai3 = AI(player=player3)
# ai4 = AI(player=player4)
# ai5 = AI(player=player5)
#
# players = [player2, player3, player4, player5]

for player in players:
    player.add_chips(60)

game = GameRound(players=players, deck=deck)
# game.set_game_qty(game_qty=10)
game.set_game_qty(infinite=True)
game.play()



