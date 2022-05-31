import random

value_lookup = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}


class Card(object):
    """Class for each card within a deck.

    Attributes:
      value (str): Number/Face value of card
      suit (str): Suit of card

    Methods:
      show: Returns tuple of (car's value, card's suit)
    """
    def __init__(self, value: int, suit: str):
        self.value = value
        self.suit = suit

    def show(self):
        return (self.value, self.suit)


class Deck(object):
    """Class for deck of Card objects.

    Attributes:
      cards (list): List of card objects contained
        in Deck

    Methods:
      build: Create full (ordered) deck with all 52 cards
      shuffle: Build deck, then randomize order
      draw: Return card on "top" of deck and remove from deck
    """
    def __init__(self):
        self.build()

    def build(self):
        suits = [
            "Spades",
            "Clubs",
            "Diamonds",
            "Hearts"
        ]

        values = [str(i) for i in range(2, 11)]
        values += ["Jack", "Queen", "King", "Ace"]

        self.cards = [Card(value, suit) for value in values for suit in suits]

    def shuffle(self):
        self.build()
        cards = self.cards
        random.shuffle(cards)

    def draw(self):
        return self.cards.pop()

class Hand(object):
    """Hand class for a player's current cards.
    Used for both dealer and players.

    Args:
      cards (list): List of Card objects to start hand with

    Attributes:
      cards (list): List of cards (Card objects) currently
        in hand
      total (int): Total point value of hand currently
      card_types (set): Unique types of card currently
        in hand

    Methods:
      add: Add a card to the hand and change
        attributes to reflect new card
    """
    def __init__(self, *args):
        assert all(isinstance(i, Card) for i in args)
        self.cards = []
        self.total = 0
        self.card_types = set()

        # Add any initalized cards
        for i in args:
            self.add(i)

    def add(self, card):
        """Add card to hand.

        Args:
          card (Card): Card object to add to hand
        """
        card_type = card.show()[0]
        card_value = value_lookup.get(card_type)
        self.cards.append(card)
        self.total += card_value
        self.card_types.add(card_type)

