from __future__ import annotations
from .card import Card
from .stack import Stack
import numpy as np

class Hand:
    cards: list[Card]
    
    def __init__(self, cards: list[Card]):
        self.cards = cards
        
    def __iadd__(self, card: Card) -> Hand:
        """
        Succinct command to add card to existing hand.

        Args:
            card (Card): Card to be added to hand.

        Returns:
            Hand: Hand after adding new card.
        """
        self.cards.append(card)
        return(self)
    
    def __mod__(self, suit: int) -> int:
        """
        Check number of cards in hand with a given suit.

        Args:
            suit (int): Suit to check for.

        Returns:
            int: Number of cards in hand with suit.
        """
        count = 0
        
        for card in self.cards:
            if (card.suit == suit):
                count += 1
                
        return count
    
    def fifteen_points(self, indices: list[int] = [], points: int = 0) -> int:
        
        if not indices:
            low = 0
            
        else:
            low = np.max(indices) + 1
        
        for i in range(low, len(self.cards)):
            print(f"i = {i}")
            card_set = Stack([self.cards[j] for j in indices] + [self.cards[i]])
            print(card_set.cards)
            
            #If current cards add to exactly fifteen, they score 2 fifteen points.
            if(+card_set == 15):
                points += 2
            
            #If current set of cards adds to less than 15, adding another card may form a fifteen.
            elif(+card_set < 15):
                indices.append(i)
                points = self.fifteen_points(indices, points)
                indices.pop()
        
        return points
    
    def pair_points(self) -> int:
        """
        Calculate pair points for hand.

        Returns:
            int: Number of points hand scores from pairs.
        """
        points = 0
        
        for i in range(len(self.cards)-1):
            for j in range(i+1,len(self.cards)):
                if(self.cards[i] - self.cards[j] == 0):
                    points += 2
            
        return points