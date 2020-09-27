from tkinter import *
from PIL import ImageTk, Image

from poker.card import Card
from poker.card_deck import CardDeck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound
from poker.ai import AI
from poker.human_player import Human, is_number

import os



class PokerGUI:
    def __init__(self):
        dir_name = os.path.dirname(__file__)
        # filename = os.path.join(dir_name, 'relative/path/to/file/you/want')
        print(dir_name)
        self._players = []
        self._root = Tk()
        # self._img_folder = r"E:\Python Course\Python\Incomplete\learn-to-code-with-python\GUI\PNG"
        # self._card_back_Image = Image.open(r"E:\Python Course\Python\Incomplete\learn-to-code-with-python\GUI\PNG"
        #                                    r"\gray_back.png")
        self._img_folder = os.path.join(dir_name, 'PNG')
        self._card_back_Image = Image.open(str(os.path.join(self._img_folder, 'gray_back.png')))
        self._my_img = self.resize_image(self._card_back_Image)
        self._root.iconbitmap(str(os.path.join(dir_name, 'card.ico')))
        self._root.title("Texas Holdem")
        self._frame = LabelFrame(self._root, padx=50, pady=50)
        self._frame.grid(row=0, column=0, padx=10, pady=10)
        self._main()

    def _main(self):
        self._quit_button()
        self._create_player_buttons()
        self.show_player_buttons()
        self._create_community_card_labels()
        self.show_community_cards()
        self._create_player_card_labels()
        self.show_player_card_labels()
        self._create_bet_buttons()
        self.show_bet_buttons()
        self._root.mainloop()

    def _quit_button(self):
        self._button_quit = Button(self._frame, text="Exit", command=self._root.quit)
        self._button_quit.grid(row=0, column=10)

    def _create_player_buttons(self):
        self._button_2_player = Button(self._frame, text="2 Players", command=lambda: self._create_players(1))
        self._button_3_player = Button(self._frame, text="3 Players", command=lambda: self._create_players(2))
        self._button_4_player = Button(self._frame, text="4 Players", command=lambda: self._create_players(3))
        self._button_5_player = Button(self._frame, text="5 Players", command=lambda: self._create_players(4))

    def _create_bet_buttons(self):
        self._button_bet = Button(self._frame, text="Bet", command=lambda: self._bet())
        self._button_check = Button(self._frame, text="Check", command=lambda: self._bet())
        self._button_raise = Button(self._frame, text="Raise", command=lambda: self._bet())

    def _create_community_card_labels(self):
        self._community_card_1 = Label(self._frame, image=self._my_img)
        self._community_card_2 = Label(self._frame, image=self._my_img)
        self._community_card_3 = Label(self._frame, image=self._my_img)
        self._community_card_4 = Label(self._frame, image=self._my_img)
        self._community_card_5 = Label(self._frame, image=self._my_img)

    def _create_player_card_labels(self):
        self._player_card_1 = Label(self._frame, image=self._my_img)
        self._player_card_2 = Label(self._frame, image=self._my_img)

    def show_player_buttons(self):
        self._button_2_player.grid(row=3, column=1)
        self._button_3_player.grid(row=3, column=2)
        self._button_4_player.grid(row=3, column=3)
        self._button_5_player.grid(row=3, column=4)

    def show_bet_buttons(self):
        self._button_bet.grid(row=15, column=3)
        self._button_check.grid(row=15, column=4)
        self._button_raise.grid(row=15, column=5)

    def show_community_cards(self):
        self._community_card_1.grid(row=10, column=1)
        self._community_card_2.grid(row=10, column=2)
        self._community_card_3.grid(row=10, column=3)
        self._community_card_4.grid(row=10, column=4)
        self._community_card_5.grid(row=10, column=5)

    def show_player_card_labels(self):
        self._player_card_1.grid(row=11, column=1, rowspan=5)
        self._player_card_2.grid(row=11, column=2, rowspan=5)

    def hide_player_buttons(self):
        self._button_2_player.grid_forget()
        self._button_3_player.grid_forget()
        self._button_4_player.grid_forget()
        self._button_5_player.grid_forget()

    def hide_bet_buttons(self):
        self._button_bet.grid_forget()
        self._button_check.grid_forget()
        self._button_raise.grid_forget()

    def hide_community_cards(self):
        self._community_card_1.grid_forget()
        self._community_card_2.grid_forget()
        self._community_card_3.grid_forget()
        self._community_card_4.grid_forget()
        self._community_card_5.grid_forget()

    def hide_player_card_labels(self):
        self._player_card_1.grid_forget()
        self._player_card_2.grid_forget()

    def _bet(self):
        return

    def _create_players(self, number):
        deck = CardDeck()
        cards = Card.create_cards()
        deck.add_cards(cards)
        hand = Hand()
        player = Player(f"Player", hand)
        self._players.append(player)
        human = Human(player=player)
        for i in range(number):
            hand = Hand()
            player = Player(f"Opponent {i}", hand)
            self._players.append(player)
            ai = AI(player=player)
        self.hide_player_buttons()
        for player in self._players:
            player.add_chips(60)
        game = GameRound(players=self._players, deck=deck)
        # game.set_game_qty(game_qty=10)
        game.set_game_qty(infinite=True)
        game.play()

    def change_image(self, img, pic):
        img = Label(self._frame, image=pic)
        return img

    @staticmethod
    def resize_image(img):
        # (691, 1056)
        resized = img.resize((86, 132), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(resized)
        return pic


main = PokerGUI()
