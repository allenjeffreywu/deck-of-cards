import random
from typing import Set

"""
Created by: Allen Wu
cards.py simulates a deck of cards
"""

"""Class Card represents a card in the deck"""


class Card:
    def __init__(self, suit_name: str, rank: int):
        """
        Creates a card
        :param suit_name: str name of the card
        :param rank: int rank of the card, 11 = J, 12 = Q, 13 = K
        """
        self.suit_name = suit_name
        self.rank = rank

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.suit_name == other.suit_name and self.rank == other.rank

    def __gt__(self, other):
        """ there is a __lt__ that is inversely related to gt (greater than). This is compareTo"""
        if self.suit_name == other.suit_name:
            return self.rank > other.rank
        else:
            return self.suit_name > other.suit_name

    def __hash__(self):
        return hash((self.suit_name, self.rank))

    def __repr__(self):
        """ there is a __str__ that can be implemented, but this overrides it if not"""
        return self.suit_name + str(self.rank)


"""Class Deck represents a Deck"""


class Deck:
    CLUB = "club"
    DIAMOND = "diamond"
    HEART = "heart"
    SPADE = "spade"

    def __init__(self):
        self.deck = set()
        for r in range(1, 14):
            self.deck.add(Card(self.CLUB, r))
            self.deck.add(Card(self.DIAMOND, r))
            self.deck.add(Card(self.HEART, r))
            self.deck.add(Card(self.SPADE, r))

    def draw_card(self) -> Card:
        """
        draw_card removes a Card from the Deck. The Deck is always shuffled.
        :return: the Card
        """
        card = random.choice(list(self.deck))
        self.deck.remove(card)
        return card

    def get_deck(self) -> Set:
        return self.deck


"""Class DeckWithJokers represents a Deck with Jokers"""


class DeckWithJokers(Deck):
    JOKER = "joker"

    def __init__(self):
        super().__init__()
        self.deck.add(Card(self.JOKER, 1))
        self.deck.add(Card(self.JOKER, 2))
