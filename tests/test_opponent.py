import pytest

from core.opponent import Opponent
from core.deck import Deck
from core.hand import Hand

def foxglove(size: int) -> Opponent:
    r_hand = Hand(Deck(13,5).cards[0:size])
    fox = Opponent("Foxglove")
    fox.hand = r_hand
    return fox

@pytest.mark.parametrize("size", [5,6])

#Verify that all probabilities in the decision matrix sum to 1.
def test_random_decision_matrix_checksum(size: int):
    opp = foxglove(size)
    mat = opp.randomDecisionMatrix()
    assert mat.sum() == 1

@pytest.mark.parametrize("size", [5,6])

def test_choose_throw_card_simple(size: int):
    opp = foxglove(size)
    assert len(opp.choose_throw_card()) == size - 4
