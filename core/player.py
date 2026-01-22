from .hand import Hand

class Player:
    name: str #Display name of player.
    hand: Hand #Current hand of player.
    points: int #Number of points the player has in the current game.

    def __init__(self, name: str):
        self.name = name
        self.hand = Hand([])
        self.points = 0

    def throw_card(self, index: int, crib: Hand) -> None:
        """
        Throw card from player's hand into crib.

        Args:
            index (int): Index of card to b thrown into crib.
            crib (Hand): Current state of crib.
        """
        crib += self.hand.cards.pop(index)
