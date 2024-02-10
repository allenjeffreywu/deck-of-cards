"""
Created by: Allen Wu
poker_hands.py identifies poker_hands given a set of cards
"""
from typing import Set, Tuple

from src.common.cards import Card

# kicker - card that is not part of the hand but can be used to break ties
# Aces are higher than kings

ROYAL_FLUSH = 10
STRAIGHT_FLUSH = 9
FOUR_OF_A_KIND = 8
FULL_HOUSE = 7
FLUSH = 6
STRAIGHT = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

HAND_SIZE = 5


def determine_poker_hand(self, hole_cards: Set[Card], river: Set[Card]) -> int:
    # TODO implement
    pass


def is_royal_flush(cards: Set[Card]) -> Tuple[bool, Set[Card]]:
    suit_dict = {}
    for card in cards:
        if card.suit_name not in suit_dict:
            suit_dict[card.suit_name] = [card]
        else:
            suit_dict[card.suit_name].append(card)
    flush_hand = None
    for key in suit_dict.keys():
        if len(suit_dict[key]) > 5:
            flush_hand = suit_dict[key]
    if flush_hand is None:
        return False, set()
    royal_flush_ranks = {10, 11, 12, 13, 1}
    winning_hand = set()
    for card in flush_hand:
        if card.rank in royal_flush_ranks:
            royal_flush_ranks.remove(card.rank)
            winning_hand.add(card)
    if not royal_flush_ranks:
        return True, winning_hand
    return False, set()


def is_flush(cards: Set[Card]) -> Tuple[bool, list[Card]]:
    """
    is_flush checks if the current hand contains a flush and returns it if it does
    :param cards: Set[Card] that will be checked for flush. Reliant on HAND_SIZE
    :return: Tuple[bool, list[Card]] If True, the list will have the flush hand.
                                     If False, the list will be empty
    """
    suit_dict = {}
    for card in cards:
        if card.suit_name not in suit_dict:
            suit_dict[card.suit_name] = [card]
        else:
            suit_dict[card.suit_name].append(card)
    flush_hand = None
    for key in suit_dict.keys():
        if len(suit_dict[key]) >= HAND_SIZE:
            flush_hand = suit_dict[key]
    if flush_hand is None:
        return False, []
    return True, sorted(flush_hand)
