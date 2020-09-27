from tkinter import *
from PIL import ImageTk, Image

from poker.card import Card
from poker.card_deck import CardDeck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound
from poker.ai import AI
from poker.human_player import Human, is_number
from time import sleep
from poker.images import get_file_names_from_directory

import os


class PokerGUI:
    def __init__(self):
        self._root = Tk()
        dir_name = os.path.dirname(__file__)
        print(dir_name)
        self._root.iconbitmap(str(os.path.join(dir_name, 'card.ico')))
        self._root.title("Texas Holdem")
        self._frame = LabelFrame(self._root, padx=50, pady=50)
        self._frame.grid(row=0, column=0, padx=10, pady=10)
        self._answer = ""
        self._wait_for_responce = False
        self._players = []
        self._img_folder = os.path.join(dir_name, 'PNG')
        self.create_image_dictionary()
        self._card_back_Image = Image.open(str(os.path.join(self._img_folder, 'gray_back.png')))
        self._my_img = self.resize_image(self._card_back_Image)
        # self._my_img  = self.resize_image(Image.open(r"C:/Users/Sarah/PycharmProjects/Texas_Holdem/PNG/7C.png"))
        self.new_image = self.resize_image(Image.open(r"C:/Users/Sarah/PycharmProjects/Texas_Holdem/PNG/7C.png"))
        self._main()

    def create_image_dictionary(self):
        self._image_dic = {}
        for file in get_file_names_from_directory(self._img_folder):
            print(file)
            self._image_dic.setdefault(file, self.resize_image(Image.open(os.path.join(self._img_folder, file))))

    def _main(self):
        self._quit_button()
        self._create_player_buttons()
        self.show_player_buttons()
        self._create_community_card_labels()
        self.show_community_cards_labels()
        self._create_player_card_labels()
        self.show_player_card_labels()
        self._create_bet_buttons()
        # self.show_bet_buttons()
        self._root.mainloop()

    def _quit_button(self):
        self._button_quit = Button(self._frame, text="Exit", command=lambda: self.stop())
        self._button_quit.grid(row=0, column=10)

    def stop(self):
        self._answer = "stop"
        self._wait_for_responce = False
        self._root.quit()
        exit()

    def _create_money_slider(self, max_value):
        self.slider = Scale(self._frame, from_=1, to=max_value, orient=HORIZONTAL)
        self._button_bet_money = Button(self._frame, text="Bet", command=lambda: self._bet_money())

    def _create_player_buttons(self):
        self._button_2_player = Button(self._frame, text="2 Players", command=lambda: self._create_players(1))
        self._button_3_player = Button(self._frame, text="3 Players", command=lambda: self._create_players(2))
        self._button_4_player = Button(self._frame, text="4 Players", command=lambda: self._create_players(3))
        self._button_5_player = Button(self._frame, text="5 Players", command=lambda: self._create_players(4))

    def _create_bet_buttons(self):
        # call / raise / fold
        # bet / check / fold
        # all in / fold
        self._button_bet = Button(self._frame, text="Bet", command=lambda: self._bet(1))
        self._button_check = Button(self._frame, text="Check", command=lambda: self._bet(2))
        self._button_raise = Button(self._frame, text="Raise", command=lambda: self._bet(3))
        self._button_fold = Button(self._frame, text="Fold", command=lambda: self._bet(4))
        self._button_call = Button(self._frame, text="Call", command=lambda: self._bet(5))
        self._button_all_in = Button(self._frame, text="All In", command=lambda: self._bet(6))

    def _create_community_card_labels(self):
        self._community_card_1 = Label(self._frame, image=self._my_img)
        self._community_card_2 = Label(self._frame, image=self._my_img)
        self._community_card_3 = Label(self._frame, image=self._my_img)
        self._community_card_4 = Label(self._frame, image=self._my_img)
        self._community_card_5 = Label(self._frame, image=self._my_img)

    def _create_player_card_labels(self):
        self._player_card_1 = Label(self._frame, image=self._my_img)
        self._player_card_2 = Label(self._frame, image=self._my_img)

    def _show_money_slider(self):
        self.slider.grid(row=11, column=4)
        self._button_bet_money.grid(row=13, column=4)

    def show_player_buttons(self):
        self._button_2_player.grid(row=3, column=1)
        self._button_3_player.grid(row=3, column=2)
        self._button_4_player.grid(row=3, column=3)
        self._button_5_player.grid(row=3, column=4)

    # call / raise / fold
    def show_call_raise_fold_buttons(self):
        self._button_call.grid(row=15, column=3)
        self._button_raise.grid(row=15, column=4)
        self._button_fold.grid(row=15, column=5)
        self._root.update()

    # all in / fold
    def show_all_in_fold_buttons(self):
        self._button_all_in.grid(row=15, column=3)
        self._button_fold.grid(row=15, column=5)
        self._root.update()

    # check / bet /  fold
    def show_check_bet_fold_buttons(self):
        self._button_check.grid(row=15, column=3)
        self._button_bet.grid(row=15, column=4)
        self._button_fold.grid(row=15, column=5)
        self._root.update()

    def show_community_cards_labels(self):
        self._community_card_1.grid(row=10, column=1)
        self._community_card_2.grid(row=10, column=2)
        self._community_card_3.grid(row=10, column=3)
        self._community_card_4.grid(row=10, column=4)
        self._community_card_5.grid(row=10, column=5)
        self._root.update()

    def show_player_card_labels(self):
        self._player_card_1.grid(row=11, column=1, rowspan=5)
        self._player_card_2.grid(row=11, column=2, rowspan=5)
        self._root.update()

    def destroy_money_slider(self):
        self.slider.destroy()
        self._button_bet_money.destroy()
        self._root.update()

    def hide_player_buttons(self):
        self._button_2_player.grid_forget()
        self._button_3_player.grid_forget()
        self._button_4_player.grid_forget()
        self._button_5_player.grid_forget()
        self._root.update()

    # call / raise / fold
    def hide_call_raise_fold_buttons(self):
        self._button_call.grid_forget()
        self._button_raise.grid_forget()
        self._button_fold.grid_forget()
        self._root.update()

    # all in / fold
    def hide_all_in_fold_buttons(self):
        self._button_all_in.grid_forget()
        self._button_fold.grid_forget()
        self._root.update()

    # check / bet /  fold
    def hide_check_bet_fold_buttons(self):
        self._button_check.grid_forget()
        self._button_bet.grid_forget()
        self._button_fold.grid_forget()
        self._root.update()

    def hide_community_cards(self):
        self._community_card_1.grid_forget()
        self._community_card_2.grid_forget()
        self._community_card_3.grid_forget()
        self._community_card_4.grid_forget()
        self._community_card_5.grid_forget()
        self._root.update()

    def hide_player_card_labels(self):
        self._player_card_1.grid_forget()
        self._player_card_2.grid_forget()
        self._root.update()

    def _bet(self, answer):
        self._answer = str(answer)
        self._wait_for_responce = False
        return

    def check(self):
        self._wait_for_responce = True
        self.show_check_bet_fold_buttons()
        self._root.update()
        while self._wait_for_responce:
            self._root.update()
            sleep(.1)
        self.hide_check_bet_fold_buttons()
        return self._answer

    def bet(self):
        self._wait_for_responce = True
        self.show_call_raise_fold_buttons()
        self._root.update()
        while self._wait_for_responce:
            self._root.update()
            sleep(.1)
        self.hide_call_raise_fold_buttons()
        return self._answer

    def make_a_bet(self, chips):
        self._wait_for_responce = True
        self._create_money_slider(chips)
        self._show_money_slider()
        while self._wait_for_responce:
            self._root.update()
            sleep(.1)
        return self._answer

    def all_in(self, chips):
        self._wait_for_responce = True
        self.show_all_in_fold_buttons()
        while self._wait_for_responce:
            self._root.update()
            sleep(.1)
        return self._answer

    def _bet_money(self):
        self._answer = str(self.slider.get())
        self.destroy_money_slider()
        self._wait_for_responce = False
        return

    def _create_players(self, number):
        self.hide_player_buttons()
        self._root.update()
        deck = CardDeck()
        cards = Card.create_cards()
        deck.add_cards(cards)
        hand = Hand()
        player = Player(f"Player", hand)
        self._players.append(player)
        human = Human(player=player, gui=self)
        for i in range(number):
            hand = Hand()
            player = Player(f"Opponent {i + 1}", hand)
            self._players.append(player)
            ai = AI(player=player)
        self.hide_player_buttons()
        for player in self._players:
            player.add_chips(60)
        game = GameRound(players=self._players, deck=deck, gui=self)
        # game.set_game_qty(game_qty=10)
        game.set_game_qty(infinite=True)
        game.play()

    def change_card_image(self, card, image_name):
        # image_name = f"/{rank[0]}{suit[0]}.png"
        img = self._image_dic[image_name]
        print(image_name)
        if card == "C1":
            # self._community_card_1.destroy()
            self._community_card_1.config(image=img)
            # self._community_card_1.grid(row=10, column=1)
        elif card == "C2":
            # self._community_card_2.destroy()
            self._community_card_2.config(image=img)
            # self._community_card_2.grid(row=10, column=2)
        elif card == "C3":
            # self._community_card_3.destroy()
            self._community_card_3.config(image=img)
            # self._community_card_3.grid(row=10, column=3)
        elif card == "C4":
            # self._community_card_4.destroy()
            self._community_card_4.config(image=img)
            # self._community_card_4.grid(row=10, column=4)
        elif card == "C5":
            # self._community_card_5.destroy()
            self._community_card_5.config(image=img)
            # self._community_card_5.grid(row=10, column=5)
        elif card == "P1":
            # self._player_card_1.grid_forget()
            self._player_card_1.config(image=img)
            # self._player_card_1.grid(row=11, column=1, rowspan=5)
        elif card == "P2":
            # self._player_card_2.grid_forget()
            self._player_card_2.config(image=img)
            # self._player_card_2.grid(row=11, column=2, rowspan=5)
        self._root.update()

    # def change_image(self, pic):
    #     resize = self.resize_image(pic)
    #     img = Label(self._frame, image=resize)
    #     return img

    def resize_image(self, img):
        # (691, 1056)
        resized = img.resize((86, 132), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(resized, master=self._frame)
        return pic


main = PokerGUI()
