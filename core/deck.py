import random

from .card import Card

class Deck:
    cards: list[Card]

    def __init__(self, ranks: int, suits:int):
        #Generate random sequence of integers from 0 to number of cards in the deck - 1.
        seq = random.sample([i for i in range(suits*ranks)], k = suits*ranks)

        #Build shuffled deck by assigning each integer n in seq to corresponding card such that n = card.suit*ranks + card.rank
        self.cards = [Card(i % ranks, i // ranks) for i in seq]

    def __contains__(self, other: Card) -> bool:
        #Check every card in deck against target card.
        for card in self.cards:
            #If both rank and suit of card match other, other is contained within the deck.
            if(card - other == 0 and card & other):
                return True

        return False
