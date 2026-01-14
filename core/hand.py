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
    
        for i in range(np.max(indices) + 1, len(self.cards)):
            indices.append(i)
            card_set = Stack([self.cards[j] for j in indices])
            
            #If current cards add to exactly fifteen, they score 2 fifteen points.
            if(+card_set == 15):
                return points + 2
            
            #If current set of cards adds to less than 15, adding another card may form a fifteen.
            elif(+card_set < 15):
                points = self.fifteen_points(indices, points)
        
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
    
    def flush_points(self) -> int:
        """
        Calculate points from flushes in hand.

        Args:
            hand (Hand): Hand to check for flush points

        Returns:
            int: Number of flush points that this hand awards
        """
        #Since a flush must have at least four cards, we only need to check the suits of the first two cards of five for a flush.
        same_suits = np.max(self % self.cards[0].suit, self % self.cards[1].suit)
        
        #If we found at least four cards with the same suit, the hand scores flush points
        if (same_suits >= 4):
            return same_suits
            
        return 0

    def ring_points(self) -> int:
        """
        Calculate number of ring points. A ring is a collection of five cards, all of different suits.
        
        Rings are exclusive to Sevian cribbage, as 'standard' decks have only four suits.

        Args:
            hand (Hand): Hand to be checked for ring points

        Returns:
            int: Number of rings points hand awards. 5 if a ring is formed, 0 otherwise.
        """
        
        #Compare suits of every pair of cards in hand.
        for i in range(len(self.cards)-1):
            for j in range(i+1,len(self.cards)):
                #If any pair of cards has the same suit, a ring is NOT formed and no points are awarded.
                if (self.cards[i] & self.cards[j]):
                    return 0
        
        return 5
    
    def eyes_points(self, cut: Card) -> int:
        """
        Calculate points from Eyes (suit of king/eye in hand matches suit of cut card).

        Args:
            hand (Hand): Hand to check for Eyes
            cut (Card): Cut card in the current round.

        Returns:
            int: Number of points scored for Eyes.
        """
        
        for card in self.cards:
            #If card is both a king and matches the suit of the cut card, score one point for Eyes.
            if (card & cut and card.rank == 12):
                return 1
        
        return 0