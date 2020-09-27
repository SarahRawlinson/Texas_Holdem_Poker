class Card:
    SUITS = ("Hearts", "Spades", "Diamonds", "Clubs")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
    _rank_value = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "Jack": 10, "Queen": 11,
                   "King": 12, "Ace": 13}

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

    @classmethod
    def create_cards(cls):
        return [
            cls(rank=rank, suit=suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __value__(self):
        return self._rank_value[self.rank]

    def __lt__(self, other):
        return self.value < other.value

    def file_name(self):
        if self.rank == "10":
            return self.rank + self.suit[0] +  ".png"
        return self.rank[0] + self.suit[0] + ".png"

    value = property(__value__)
