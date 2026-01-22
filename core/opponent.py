from .hand import Hand
from .player import Player

class Opponent(Player):
    name: str #Display name of player.
    hand: Hand #Current hand of player.
    points: int #Number of points the player has in the current game.

    #Properties not yet implemented:
    behaviour: list[int] #Weightings for types of decision methods opponent uses to pick which cards to throw away.
    dialogue: list[str] #Set of dialogue lines that opponent may say during play.

    def __init__(self, name: str, behaviour: list[int] = [], dialogue: list[str] = []): #pylint: disable=dangerous-default-value
        super().__init__(name)
        self.behaviour = behaviour
        self.dialogue = dialogue
