from random import shuffle

SUITS = {"s": "spades", "d": "dimonds", "h": "hearts", "c": "clubs"}
NUMBERS = {
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "jack",
    12: "queen",
    13: "king",
    14: "ace",
}


class Deck:
    """Represents a deck of 52 cards. 4 suits and 13 cards"""

    def __init__(self) -> None:
        self.cards = []

        # Build deck
        for suit in SUITS:
            for number in NUMBERS:
                self.cards.append(Card(suit, number))

        # Shuffle deck
        self._shuffle()

    def _shuffle(self):
        shuffle(self.cards)

    def num_cards(self) -> int:
        """Return number of cards left in deck"""
        return len(self.cards)

    def draw_card(self):
        """Return next card in the deck"""
        return self.cards.pop()


class Card:
    """
    A single card with a number and a suit.

    11 = Jack
    12 = Queen
    13 = King
    14 = Ace
    """

    def __init__(self, suit: str, number: int) -> None:

        # Check for valid input
        if suit not in ["s", "d", "h", "c"]:
            raise ValueError(
                "Must be valid suit. \n\nUseage: (s = 'spades'), (d = 'dimonds'), (h = 'hearts'), (c = 'clubs')"
            )
        if number not in list(NUMBERS.keys()):
            raise ValueError(
                "Card numbers are from 2-14 (11 = jack) (12 = queen) (13 = king) (14 = ace)"
            )

        self.number = number
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.get_number()} of {self.get_suit()}"

    def __lt__(self, other_card):
        if self.number < other_card.number:
            return True
        return False

    def __le__(self, other_card):
        if self.number <= other_card.number:
            return True
        return False

    def __gt__(self, other_card):
        if self.number > other_card.number:
            return True
        return False

    def __ge__(self, other_card):
        if self.number >= other_card.number:
            return True
        return False

    def __eq__(self, other_card):
        if self.number == other_card.number:
            return True
        return False

    def get_suit(self) -> str:
        return SUITS[self.suit]

    def get_number(self) -> str:
        return NUMBERS[self.number]


if __name__ == "__main__":
    deck = Deck()
    print(deck.num_cards())
    print(deck.pop())
    print(deck.num_cards())
