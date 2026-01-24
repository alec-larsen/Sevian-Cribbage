import random

import numpy as np

from .hand import Hand
from .player import Player

class Opponent(Player):
    name: str #Display name of player.
    hand: Hand #Current hand of player.
    points: int #Number of points the player has in the current game.

    #Properties not yet implemented:
    behaviour: list[int] #Weightings for types of decision methods opponent uses to pick which cards to throw away.
    dialogue: list[str] #Set of dialogue lines that opponent may say during play.

    def __init__(self, name: str, behaviour: list[int] = [1], dialogue: list[str] = NotImplemented): #pylint: disable=dangerous-default-value
        super().__init__(name)
        self.behaviour = behaviour
        self.dialogue = dialogue

    #Decision matrix generators
    def randomDecisionMatrix(self) -> np.typing.NDArray[np.float64]:
        """
        Generate decision matrix for choosing random card to throw into crib.
        
        Will return a vector if one one card is to be thrown and a matrix if two cards must be thrown.
        
        Assumptions:
            - player hand (self.hand) has a size of 5 or 6

        Returns:
            np.ndarray: Decision matrix for throwing card into crib.
        """
        #If hand is of size 5, only one card needs to be thrown.
        if len(self.hand) == 5:
            return np.ones(5)/5

        #Else, hand is of size 6 and we must throw away two cards.
        else:
            return np.triu(np.ones(shape=(6,6)),k=1)/15

    def choose_throw_card(self)->list[int]:
        """
        Using above decision matrix generators, determine which cards opponent will throw into crib.

        Returns:
            list[int]: Indices of cards in hand to be thrown into crib; size 1 if player hand is 5 cards, else size 2.
        """
        #Package decision functions defined above into a single list for use of list comprehension
        DECISION_FUNCTIONS = [self.randomDecisionMatrix]
        #The overall decisionm matrix is the sum of each decision matrix times the weight given to each type of decision by the specific player.
        decision = sum([dec()*self.behaviour for dec in DECISION_FUNCTIONS])
        indices = np.argwhere(decision == np.max(decision))
        return random.choice(indices)
