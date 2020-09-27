import random


class CardDeck:
    def __init__(self):
        self.cards = []
        
    def __len__(self):
        return len(self.cards)

    def add_cards(self, cards: []):
        self.cards.extend(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_cards(self, number_to_deal):
        cards = self.cards[:number_to_deal]
        del self.cards[:number_to_deal]
        return cards

