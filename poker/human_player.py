def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class Human:
    def __init__(self, player, gui):
        self._gui = gui
        self.name = "Human"
        self.fold = False
        self.player = player
        self.wants_to_bet = False
        self.check = True
        self.call = True
        self.bet_qty = 0
        self.all_in = False
        self.raise_bet = False
        player.controller = self

    def update(self, number):
        self._gui.update_text_labels_hand(self.player.hand.hand)
        if number > 0:
            self.show_new_cards()

    def show_new_cards(self):
        cards = self.player.starting_hand_suit_rank()
        print(cards[0].file_name())
        print(cards[1].file_name())
        self._gui.change_card_image("P1", cards[0].file_name())
        self._gui.change_card_image("P2", cards[1].file_name())


    def make_decision(self, bet, total_bet):
        # self.show_new_cards()
        if bet > 0:
            if self.raise_bet:
                self.wants_to_bet = True
                self.bet()
        else:
            waiting_for_responce = True
            while waiting_for_responce:
                # answer = input(f"Your card value is {self.player.hand.score}, would you like to bet? 1: Yes, 2: No, "
                #                f"3: Fold\n")
                answer = self._gui.check()

                if answer == "1":  # bet
                    # print(f"{self.player.name} thinks they should bet")
                    self.wants_to_bet = True
                    self.check = False
                    waiting_for_responce = False
                    self.bet()
                elif answer == "2":  # check
                    # print(f"{self.player.name} decides not to bet")
                    self.wants_to_bet = False
                    self.check = True
                    waiting_for_responce = False
                elif answer == "4":  # fold
                    # print(f"{self.player.name} wants to fold")
                    self.wants_to_bet = False
                    self.player.fold()
                    waiting_for_responce = False
                else:
                    print("Answer not valid, please try again")

    def bet(self):
        card_amount = len(self.player.hand.cards)
        card_value = self.player.hand.score
        waiting_for_answer = True
        amount_to_bet = 0
        while waiting_for_answer:
            # amount_to_bet = input("How much would you like to bet? \n")
            amount_to_bet = self._gui.make_a_bet(self.player.chips)
            if is_number(amount_to_bet):
                if int(amount_to_bet) <= self.player.chips:
                    waiting_for_answer = False
                    amount_to_bet = int(amount_to_bet)

        # print(f"{self.player.name} thinks they should bet {amount_to_bet}")
        if amount_to_bet > self.player.chips:
            amount_to_bet = self.player.chips
        self.bet_qty = amount_to_bet

    def check_for_call(self, amount, total_bet):
        card_amount = len(self.player.hand.cards)
        card_value = self.player.hand.score
        call = False
        raise_bet = False
        all_in = False
        fold = False
        waiting_for_response = True
        while waiting_for_response:
            if amount > self.player.chips:
                # answer = input("the bet is more than you have would you like to go all in or fold? 1: All in, "
                #                "2: Fold \n")
                answer = self._gui.all_in()
                if answer == "6":
                    all_in = True
                    waiting_for_response = False
                elif answer == "4":
                    fold = True
                    waiting_for_response = False
            else:
                # answer = input(f"your cards value is {card_value}, you need to have already bet {total_bet} you need "
                #                f"to bet at least {amount} chips. would you like to 1: Call, 2:Fold, 3: Raise? \n")
                answer = self._gui.bet()
                if answer == "5":
                    call = True
                    waiting_for_response = False
                elif answer == "4":
                    fold = True
                    waiting_for_response = False
                elif answer == "3":
                    raise_bet = True
                    waiting_for_response = False
            if waiting_for_response:
                print("No Valid Response, please try again")
        self.call = call
        self.all_in = all_in
        self.raise_bet = raise_bet
        self.fold = fold
        # if raise_bet:
        #     print(f"{self.player.name} thinks they should raise")
        # elif call:
        #     print(f"{self.player.name} thinks they should call")
        # elif all_in:
        #     print(f"{self.player.name} thinks they should go all in")
        # elif fold:
        #     print(f"{self.player.name} thinks they should fold")
