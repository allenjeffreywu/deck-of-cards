import unittest

from src.common.cards import Card, Deck

"""
Created by: Allen Wu
cards_test.py tests cards' Card and Deck implementations
"""


class CardTest(unittest.TestCase):
    SUIT_1 = "suit1"
    SUIT_2 = "suit2"

    def test_card_eq(self):
        card_1 = Card(self.SUIT_1, 1)
        card_2 = Card(self.SUIT_2, 2)
        self.assertNotEqual(card_1, card_2)

    def test_card_gt(self):
        card_1 = Card(self.SUIT_1, 1)
        card_2 = Card(self.SUIT_1, 2)
        self.assertTrue(card_2 > card_1)


class DeckTest(unittest.TestCase):
    DECK_SIZE = 52

    def test_deck_init(self):
        deck_1 = Deck()
        deck_2 = Deck()
        for val in deck_2.get_deck():
            deck_1.deck.remove(val)
        # assert that the deck is empty and has all cards
        self.assertTrue(not deck_1.get_deck())

    def test_deck_draw(self):
        deck = Deck()
        self.assertEqual(len(deck.get_deck()), self.DECK_SIZE)
        deck.draw_card()
        self.assertEqual(len(deck.get_deck()), self.DECK_SIZE - 1)


if __name__ == '__main__':
    unittest.main()
