from tkinter import *
from PIL import ImageTk, Image

from poker.card import Card
from poker.card_deck import CardDeck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound
from poker.ai import AI
from poker.human_player import Human, is_number


def resize_image(img):
    # (691, 1056)
    resized = img.resize((86, 132), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(resized)
    return pic


players = []
root = Tk()
root.title("Texas Holdem")
root.iconbitmap(r"E:\Python Course\Python\Incomplete\learn-to-code-with-python\GUI\card.ico")
im = Image.open(r"E:\Python Course\Python\Incomplete\learn-to-code-with-python\GUI\PNG\gray_back.png")

my_img = resize_image(im)

frame = LabelFrame(root, padx=50, pady=50)
frame.grid(row=0, column=0, padx=10, pady=10)

button_quit = Button(frame, text="Exit", command=root.quit)


def create_players(number):
    deck = CardDeck()
    cards = Card.create_cards()
    deck.add_cards(cards)
    hand = Hand()
    player = Player(f"Player", hand)
    players.append(player)
    human = Human(player=player)
    for i in range(number):
        hand = Hand()
        player = Player(f"Opponent {i}", hand)
        players.append(player)
        ai = AI(player=player)
    hide_buttons()
    for player in players:
        player.add_chips(60)
    game = GameRound(players=players, deck=deck)
    # game.set_game_qty(game_qty=10)
    game.set_game_qty(infinite=True)
    game.play()


def hide_buttons():
    button_2_player.grid_forget()
    button_3_player.grid_forget()
    button_4_player.grid_forget()
    button_5_player.grid_forget()
    return


def show_buttons():
    button_2_player.grid(row=3, column=1)
    button_3_player.grid(row=3, column=2)
    button_4_player.grid(row=3, column=3)
    button_5_player.grid(row=3, column=4)


def change_image(img, pic):
    img = Label(frame, image=pic)


button_2_player = Button(frame, text="2 Players", command=lambda: create_players(1))
button_3_player = Button(frame, text="3 Players", command=lambda: create_players(2))
button_4_player = Button(frame, text="4 Players", command=lambda: create_players(3))
button_5_player = Button(frame, text="5 Players", command=lambda: create_players(4))

show_buttons()

community_card_1 = Label(frame, image=my_img)
community_card_1.grid(row=10, column=1)
community_card_2 = Label(frame, image=my_img)
community_card_2.grid(row=10, column=2)
community_card_3 = Label(frame, image=my_img)
community_card_3.grid(row=10, column=3)
community_card_4 = Label(frame, image=my_img)
community_card_4.grid(row=10, column=4)
community_card_5 = Label(frame, image=my_img)
community_card_5.grid(row=10, column=5)

player_card_1 = Label(frame, image=my_img)
player_card_1.grid(row=11, column=1)
player_card_2 = Label(frame, image=my_img)
player_card_2.grid(row=11, column=2)

button_quit.grid(row=0, column=10)
root.mainloop()

# help(my_button1)
