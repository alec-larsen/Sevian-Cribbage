from .card import Card
from core import util

class Stack():
    cards: list[Card]
    
    def __init__(self, cards: list[Card]):
        self.cards = cards
    
    def __pos__(self) -> int:
        """
        Calculate total value of stack.

        Returns:
            int: Sum of values of all cards in stack.
        """
        sum = 0
        for card in self.cards:
            sum += card.value
            
        return sum
    
    def __invert__(self):
        """
        Calculate flush points in stack.
        
        A cribbage flush is worth one point per card for a minimum of four cards. For stacks, all flush cards must be at the top of the stack.
        
        Returns:
            int: Maximum number n such that the top n cards in the stack are the same suit if n >= 4. Else 0.
        """
        #If stack has less than 4 cards, a flush is impossible.
        if len(self.cards) < 4:
            return 0
        
        #Move through all cards to find the index of the first card with a DIFFERENT suit to the top card.
        for i in range(len(self.cards)):
            if not(self.cards[i] & self.cards[0]):
                #If at least top 4 cards have the same suit, flush points are awarded
                if i >= 4:
                    return i
                return 0
        
        #If this return is reached, every card in the stack has the same suit.
        return i + 1
    
    def pairs(self) -> int:
        """
        Calculate pair points on top of stack.

        Returns:
            int: Number of points scored by pairs.
        """
        points = 0
        #Loop through all but top card in stack until we hit a card without the same rank as the top card.
        for i in range(len(self.cards)):
            #If the current card we're looking at is the same rank as the top, it forms a pair for each card above it in the stack (i-1)
            if self.cards[i] - self.cards[0] == 0:
                points += 2*i
            #If the current card is a different rank, we've reached the end of the pairs.
            else:
                return points
        #If we make it to this point, all cards on the stack are the same rank.
        return points
    
    def runs(self) -> int:
        """
        Calculate run points at top of stack.

        Returns:
            int: Number of points scored from runs at the top of the stack.
        """
        points = 0
        cards: list[Card] = []
        #Loop through all possible run lengths to check for longest run on top of stack
        for card in self.cards:
            cards.append(card)
            #If top i-1 cards of stack form run, update maximum sized run
            if len(cards) >= 3 and util.is_run(cards):
                points = len(cards)
        return points
        
    def add_card(self, card: Card) -> bool:
        """
        Adds card to stack (as index 0) if allowed by Sevian Cribbage rules.

        Args:
            card (Card): Card to be added to stack.

        Returns:
            bool: True if card was successfully added to stack. False if adding card is illegal move.
        """
        if(+self + card.value > 31):
            #Return False if adding card would exceed the total allowed value of stack (31).
            return False
        
        #If we didn't return False, card can be added to stack.
        self.cards.insert(0, card)
        return True