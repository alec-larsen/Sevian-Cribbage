from __future__ import annotations
import numpy as np

RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITS = ["\u2660", "\u2663", "\u2665", "\u2666", "\u2605"]

class Card:
    rank: int #Exact rank of card i.e. J, Q, K
    value: int #Number of points card is worth when counting, i.e. J, Q, K = 10
    suit: int

    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.value = np.min([self.rank + 1, 10]) #10, J, Q, K cards are all worth 10 points in counting.
        self.suit = suit

    def __repr__(self):
        #When print call is made, print card as a tuple of its suit and rank. Built only for decks up to 5 suits and 13 ranks.
        return f"{RANKS[self.rank]}{SUITS[self.suit]}"

    def __add__(self, other: Card | int) -> int:
        """
        Add cards valuewise or adds the value of card to an existing integer total.

        Args:
            other (Card|int): Card or integer value total whose value will be added to the rank of self.

        Returns:
            int: Sum of values of self and other.
        """
        if isinstance(other, int):
            return self.value + other

        else:
            return self.value + other.value

    def __sub__(self, other: Card) -> int:
        """
        Subtract cards rankwise.

        Args:
            other (Card): Card whose rank will be subtracted from rank of self

        Returns:
            int: Difference in rank between self and other.
        """
        return self.rank - other.rank

    def __and__(self, other: Card) -> bool:
        """
        Check if cards have the same suit.

        Args:
            other (Card): Card whose suit will be compared to self.

        Returns:
            bool: True if cards have the same suit. False otherwise.
        """
        return self.suit == other.suit

    def __eq__(self, other: object) -> bool:
        """
        Check if two cards are identical; primarily used in testing.

        Args:
            other (object): Card to check for equality with

        Returns:
            bool: True if cards have same suit and same rank, False otherwise.
        """
        if not isinstance(other, Card):
            return NotImplemented

        return (self.rank == other.rank) and (self & other)
