import unittest

from src.poker.poker_hands import *

TEST_SUIT_1 = "test suit 1"
TEST_SUIT_2 = "test suit 2"


class PokerHandsTest(unittest.TestCase):
    def test_royal_flush(self):
        card_1 = Card(TEST_SUIT_1, 9)
        card_2 = Card(TEST_SUIT_1, 2)
        card_3 = Card(TEST_SUIT_1, 10)
        card_4 = Card(TEST_SUIT_1, 11)
        card_5 = Card(TEST_SUIT_1, 12)
        card_6 = Card(TEST_SUIT_1, 13)
        card_7 = Card(TEST_SUIT_1, 1)
        hand = {card_1, card_2, card_3, card_4, card_5, card_6, card_7}
        self.assertTrue(is_royal_flush(hand))
        card_1.rank = 10
        self.assertTrue(is_royal_flush(hand), "duplicate card")
        card_1.suit_name = TEST_SUIT_2
        self.assertTrue(is_royal_flush(hand), "wrong suit in hand")
        card_4.rank = 8
        self.assertFalse(is_royal_flush(hand), "no royal flush")

    def test_is_flush(self):
        card_1 = Card(TEST_SUIT_1, 9)
        card_2 = Card(TEST_SUIT_1, 2)
        card_3 = Card(TEST_SUIT_1, 10)
        card_4 = Card(TEST_SUIT_1, 11)
        card_5 = Card(TEST_SUIT_1, 12)
        card_6 = Card(TEST_SUIT_1, 13)
        card_7 = Card(TEST_SUIT_1, 1)
        hand = {card_1, card_2, card_3, card_4, card_5, card_6, card_7}

        flush_bool, flush_cards = is_flush(hand)
        self.assertTrue(flush_bool and len(flush_cards) == 7)

        card_1.suit_name = TEST_SUIT_2
        card_2.suit_name = TEST_SUIT_2
        card_3.suit_name = TEST_SUIT_2
        card_4.suit_name = TEST_SUIT_2
        flush_bool, flush_cards = is_flush(hand)
        self.assertTrue(not flush_bool and not flush_cards)



if __name__ == '__main__':
    unittest.main()
