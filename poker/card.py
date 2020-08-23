class Card():
    SUITS = ("Hearts", "Spades", "Diamonds", "Clubs")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

    def __init__(self, rank, suit):
        if str(rank) not in self.RANKS:
            raise ValueError(f"invalid error rank must be one of the following {self.RANKS}")
        if suit not in self.SUITS:
            raise ValueError(f"invalid error rank must be one of the following {self.SUITS}")

        self.rank = str(rank)
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"
