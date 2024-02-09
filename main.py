from src.common.cards import Deck

if __name__ == '__main__':
    deck = Deck()
    print(len(deck.get_deck()))
    card = deck.draw_card()
    print(len(deck.get_deck()))
    print(card)
